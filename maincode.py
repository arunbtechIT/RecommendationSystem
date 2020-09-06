import csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from bs4 import BeautifulSoup
import requests
from difflib import get_close_matches
import webbrowser
lit=[]
reco=[]
df = pd.read_csv("movie_dataset.csv")

features = ['keywords', 'cast', 'genres', 'director']
ssimilar_movies=[]
def combine_features(row):
        return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']

for feature in features:
    df[feature] = df[feature].fillna('') #filling all NaNs with blank string

df["combined_features"] = df.apply(combine_features,axis=1)
df.iloc[0].combined_features
cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(df["combined_features"]) #feeding combined strings(movie contents) to CountVectorizer() object
cosine_sim = cosine_similarity(count_matrix)
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]
movie_user_likes = "Inception"
movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index])) #accessing the row corresponding to given movie to find all the similarity scores for that movie and then enumerating over it
ssimilar_movies=sorted(similar_movies)
i=0
print("Top 5 similar movies to "+movie_user_likes+" are:\n")
for element in ssimilar_movies:
    lit.append(get_title_from_index(element[0]))
    i=i+1
    if i>5:
        break
print(lit)

try:
    
 for i in lit:
        url = ("https://yts.lt/browse-movies/" + str(i) + "")
        #print(url)
        title_arr = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        prices = []
        source_code = requests.get(url, headers=headers)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        s = soup.find_all('div', {'class': 'browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4'})
        
        for im in s:
                print (im.img['src'])
                reco.append(im.img['src'])
except:
        print() 

