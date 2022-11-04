import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=191597'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 사람이 크롤링 하는 것과 코드가 접근하는 것에 따라 결과값이 달라질 수 있다.
# 코드로 접근하는 방법 (selector 복사)
# soup.select_one('head > meta:nth-child(9)')

# selector를 사용하지 않고 태그를 가져오는 방법
# print(soup.select_one('meta[property="og:title"]')['content'])
title = soup.select_one('meta[property="og:title"]')['content']
image = soup.select_one('meta[property="og:image"]')['content']
desc = soup.select_one('meta[property="og:description"]')['content']
print(title, image, desc)

