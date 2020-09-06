from django.http import HttpResponse
from django.shortcuts import render
import csv
from bs4 import BeautifulSoup
import requests
from difflib import get_close_matches
import webbrowser

from . import views
import csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
lit=[]
reco=[]
class users():

    def __init__(self,username=None,password=None,phone=None,email=None):
      self.username=username
      self.password=password
      self.phone=phone
      self.email=email

class destination():
    def __init__(self,img=None,title=None):
        self.image=img
        self.movie_name=title


# Create your views here.

def reg(request):
    return render(request,'reg_index.html')
def reverse(request):
    return render(request,'login_index.html')


def Login(request):
    count=0
    try:
        user_name=request.GET['name']
        pass_check = request.GET['password']
        with open('users.csv', 'r+') as csvFile1:
            csv_reader=csv.reader(csvFile1)

            for row in csv_reader:
               # if (pass_check == rows[1]):
               try:
                    d=''
                    if user_name==d or pass_check==d:
                        return render(request,'login_index.html')
                    if user_name==row[0] and pass_check==row[1]:
                        count = 1
                        return render(request,'index1.html')

               except:
                    print(' ')

            if(count!=1):
               return render(request,'login_index.html')
    except:
       print ('')


def register(request):
        user_list = []
        list=[]

        username=request.GET['name']
        password=request.GET['password']
        email=request.GET['mail']
        phone=request.GET['phone']
        user_list.append(users(username=username,password=password,email=email,phone=phone))
        list=[user_list[0].username,user_list[0].password,user_list[0].phone,user_list[0].email]
        print(user_list)
        with open('users.csv', 'a') as csvFile2:
            writer = csv.writer(csvFile2)
            writer.writerow(list)
        print(list)
        d=''
        if d not in list:
                return render(request,'login_index.html')
        else:
                return render(request, 'reg_index.html')




'''def user_history(request):
    movie = request.GET['Search']
    csv_file3= csv.reader(open('movie_dataset.csv', "r+"))
    csv_file4=csv.reader(open('user_history.csv','a+'))
    for row in csv_file3:
        if movie == row[1]:
            #print(row[1])
            str1 = str(row)
            csv_file4.write(str1 + "\n")
    #f = open("file1.csv", "r")
    str = csv_file4.read()
    print(str)
    csv_file4.close()

    with open('moviespro.csv', 'a') as csvFile4:
        writer = csv.writer(csvFile4)
        writer.writerow(str1 + "\n")'''



def recomended(request):
    mlist=[]
    reco = []

    ssimilar_movies=[]
    lit=[]
    print(lit)
    df = pd.read_csv("movie_dataset.csv")

    features = ['keywords', 'cast', 'genres', 'director']

    def combine_features(row):
        return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']

    for feature in features:
        def get_title_from_index(index):
            return df[df.index == index]["title"].values[0]

        def get_index_from_title(title):
            return df[df.title == title]["index"].values[0]

        ##################################################

        ##Step 1: Read CSV File
        df = pd.read_csv("movie_dataset.csv")
        # print df.columns
        ##Step 2: Select Features

        features = ['keywords', 'cast', 'genres', 'director']
        ##Step 3: Create a column in DF which combines all selected features
        for feature in features:
            df[feature] = df[feature].fillna('')

        def combine_features(row):
            try:
                return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]
            except:
                print ("Error:", row)

        df["combined_features"] = df.apply(combine_features, axis=1)

        # print "Combined Features:", df["combined_features"].head()

        ##Step 4: Create count matrix from this new combined column
        cv = CountVectorizer()

        count_matrix = cv.fit_transform(df["combined_features"])

        ##Step 5: Compute the Cosine Similarity based on the count_matrix
        cosine_sim = cosine_similarity(count_matrix)
        movie_user_likes = request.GET['title']

        ## Step 6: Get index of this movie from its title
        movie_index = get_index_from_title(movie_user_likes)

        similar_movies = list(enumerate(cosine_sim[movie_index]))

        ## Step 7: Get a list of similar movies in descending order of similarity score
        sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

        ## Step 8: Print titles of first 50 movies
        i = 0
    for element in sorted_similar_movies:
            lit.append(get_title_from_index(element[0]))
            i = i + 1
            print(lit)
            if i > 5:
                break

    key = request.GET['title']
    url = "https://yts.lt/browse-movies/" + str(key) + ""
    title_arr = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    prices = []
    try:
        source_code = requests.get(url, headers=headers)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        s = soup.find_all('div', {'class': 'browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4'})


        imglist=[]
        for im in s:
            imglist.append(im.img['src'])

            break
        print(lit)
    except:
     print ("ee")
    for i in lit:
        url = ("https://yts.lt/browse-movies/" + str(i) + "")
        # print(url)
        title_arr = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        prices = []
        source_code = requests.get(url, headers=headers)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        s = soup.find_all('div', {'class': 'browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4'})
        i=0
        for im in s:
            reco.append(im.img['src'])
            print (im.img['src'])
            i = i + 1
            if i > 1:
               break
    dest1=[]
    for i in range(len(lit)):
        dest1.append(destination(reco[i],lit[i]))

    return  render(request,'index1.html',{'Img':imglist,'dest':dest1,'name':movie_user_likes})

def gotologin(request):
    return render(request,'login_index.html')
def gotosignup(request):
    return render(request,'reg_index.html')
def index(request):
    return render(request,'index.html')
def logout(request):
    return render(request,'index.html')
