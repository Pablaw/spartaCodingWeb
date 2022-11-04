# 순위 / 곡 제목 / 가수
#
# https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

rows = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for row in rows:
    rank = row.select_one('td.number').text.split()[0]
    title = row.select_one('td.info > a.title.ellipsis')
    if title.span is not None:
        title = title.span.extract().text+' '+title.text.strip()
    else:
        title = title.text.strip()
    singer = row.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, singer)


