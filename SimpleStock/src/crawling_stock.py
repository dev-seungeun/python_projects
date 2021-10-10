# 네이버 금융 삼성전자 데이터 수집
import requests
from bs4 import BeautifulSoup
import sys
import time


# 함수형태 변환
def get_bs_obj(com_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + com_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")  # html.parser 로 파이썬에서 쓸 수 있는 형태로 변환
    return bs_obj


# 현재가 추출
def get_price(com_code):
    bs_obj = get_bs_obj(com_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind_now = no_today.find("span", {"class": "blind"})
    return blind_now.text


try:
    while True:
        print("=================================")
        tm = time.localtime()
        string = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)
        print(string)

        # 삼성전자 005930
        print("  > 삼성전자 :", get_price("005930"))

        # 셀트리온 068270
        print("  > 셀트리온 :", get_price("068270"))

        # 카카오 035720
        print("  > 솔루엠   :", get_price("248070"))

except KeyboardInterrupt:
    sys.exit(0)  # or 1, or whatever
