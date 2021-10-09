import urllib.request  # url에 접속하기 위한 라이브러리
from bs4 import BeautifulSoup  # 웹사이트의 html이나 css같은 정보를 모두 끌어모아 주는 역할 (pip install bs4)


webpage = urllib.request.urlopen('https://www.seoul.go.kr/coronaV/coronaStatus.do')
soup = BeautifulSoup(webpage, 'html.parser')

status_korea = soup.find('div', "status-korea")
korea_datas = [status_korea.find('div', "num knum5"), status_korea.find('div', "num knum1"), status_korea.find('div', "num knum4"), status_korea.find('div', "num knum3"), status_korea.find('div', "num knum2")]

status_seoul = soup.find('div', "status-seoul")
seoul_datas = [status_seoul.find('div', "num num10"), status_seoul.find('div', "num num1"), status_seoul.find('div', "num num8"), status_seoul.find('div', "num num11"), status_seoul.find('div', "cell cell5").find('div', "num num8"), status_seoul.find('div', "num num9")]

print('=========== 대한민국 코로나 현황 ===========')
length_k_datas = len(korea_datas)
for k_idx in range(length_k_datas):
    data = korea_datas[k_idx]
    print('  ' + data.find("p", "txt").get_text() + ' : ', data.find("p", "counter").get_text())
    if k_idx == length_k_datas-1:
        print("\n")

print('=========== 서울 코로나 현황 ===========')
length_s_datas = len(seoul_datas)
for s_idx in range(length_s_datas):
    data = seoul_datas[s_idx]
    print('  ' + data.find("p", "txt").get_text() + ' : ', data.find("p", "counter").get_text())
    if s_idx == length_s_datas-1:
        print("\n")
