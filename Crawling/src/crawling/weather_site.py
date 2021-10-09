import urllib.request  # url에 접속하기 위한 라이브러리
from bs4 import BeautifulSoup  # 웹사이트의 html이나 css같은 정보를 모두 끌어모아 주는 역할 (pip install bs4)
import datetime


now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')

print('환영합니다, ' + nowDate)
print('오늘의 주요 정보를 요약해 드리겠습니다.\n')


# 오늘의 날씨
print('#오늘의 #날씨 #요약 \n')
webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('div', "temperature_text")
cast = soup.find('p', "summary")
print('  >> 서울 날씨 : ', temps.get_text(), '℃', cast.get_text())

webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%81%EC%A3%BC+%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8&tqi=hTbyOsprvN8ssNZsnGCssssssA8-352441')
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('div', "temperature_text")
cast = soup.find('p', "summary")
print('  >> 영주 날씨 : ', temps.get_text(), '℃', cast.get_text())

webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%95%88%EC%96%91+%EB%82%A0%EC%94%A8&oquery=%EC%98%81%EC%A3%BC+%EB%82%A0%EC%94%A8&tqi=hTbyPdprvh8sseBccR8ssssstYo-498652')
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find('div', "temperature_text")
cast = soup.find('p', "summary")
print('  >> 안양 날씨 : ', temps.get_text(), '℃', cast.get_text())
print('\n')
