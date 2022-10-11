import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 전체 목록을 가져오기.
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

#순위
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.number
#제목
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.title.ellipsis
#가수
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.artist.ellipsis

# 가져온 목록을 하나하나 출력하기.
for song in songs:
    rank = song.select_one('td.number').text[0:2].strip()

    title = song.select_one('td.info > a.title.ellipsis')
    # 단순 span 태그 제거 방법
    # title = song.select_one('td.info > a.title.ellipsis').text.strip().strip('19금').strip()
    # extract() 명령어 사용으로 정리하는 방법
    if title.span != None:
        print(title.span.extract().text, title.text.strip())
    else:
        print(title.text.strip())

    singer = song.select_one('td.info > a.artist.ellipsis').text