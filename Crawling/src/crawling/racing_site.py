from urllib.request import urlopen  # url에 접속하기 위한 라이브러리
from bs4 import BeautifulSoup  # 웹사이트의 html이나 css같은 정보를 모두 끌어모아 주는 역할 (pip install bs4)

'''
# pip install html_table_parser
# HTML table 태그를 긁어와서, 파이썬 데이터 프레임으로 저장할 때 유용하게 사용됨
'''
from html_table_parser import parser_functions as parser

'''
# pip install pandas
# 데이터프레임
'''
import pandas as pd



url = "http://race.kra.co.kr/raceScore/ScoretableDetailList.do?meet=1&realRcDate=20170723&realRcNo=1"

result = urlopen(url)
html = result.read()
soup = BeautifulSoup(html, 'html.parser')

temp = soup.find_all('table')

p = parser.make2d(temp[2])
df = pd.DataFrame(p[1:], columns=p[0])
print("=============== [경마] 경주별 상세 성적표 ===============")
print(df)
