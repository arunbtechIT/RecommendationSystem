#sampl1 mix sample2.
#searching content (movies)in csv file.
import csv
import sys

movie = input('search movie here:\n')
csv_file = csv.reader(open('moviespro.csv', "r+"))
f=open("file1.csv", "a+")

for row in csv_file:
	if movie == row[1]:
		print(row[1])
		str1=str(row)
		f.write(str1+"\n")
print("::Search History::")
f=open("file1.csv", "r")
str=f.read()
print(str)
f.close()

