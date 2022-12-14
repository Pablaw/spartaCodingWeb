import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://pablaw:1239282@studylog.xy5ijs9.mongodb.net/?retryWrites=true&w=majority')
db = client.pablaw

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    temp_movie = movie.select_one('td.title > div > a')
    if temp_movie is not None:
        title = temp_movie.text
        rank = movie.select_one('img')['alt']
        star = movie.select_one('td.point').text
        doc = {
            'title': title,
            'rank': rank,
            'star': star
        }
        db.movies.insert_one(doc)