import random

menus = ['김치 볶음밥', '초밥', '김치 찌개', '콩나물 국밥', '스파게티', '비빔밥', '짜장면', '칼국수', '삼계탕', '돈까스', '샐러드', '햄버거']
prices = [6000, 9000, 7000, 6000, 7000, 6000, 4000, 5000, 9000, 8000, 7000, 5000]

print('메뉴:')
for menu, price in zip(menus, prices):
    print(menu, price)
'''
김치 볶음밥 6000
초밥 9000
김치 찌개 7000
콩나물 국밥 6000
스파게티 7000
비빔밥 6000
짜장면 4000
칼국수 5000
삼계탕 9000
돈까스 8000
샐러드 7000
햄버거 5000
'''

i = random.randint(0, len(menus) - 1)
print('추천 메뉴:', menus[i])
print('메뉴 가격:', prices[i])
