# 변수선언
a = 1
b = 1.2
c = b

print(id(a), id(1), id(b), id(c))  # 주소값
print(a is b, a == b)  # False False
print(b is c, b == c)  # True True


# type
print(type("str"))  # <class 'str'>
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>

print()


# Integer arithmetic
print(10 + 10)   # 20
print(100 - 10)  # 90
print(10 * 10)   # 100
print(77 / 10)   # 7.7
print(77 // 10)  # 7

print(7 % 2)  # 1
print(8 % 2)  # 0
print(11 % 6.0)  # 5.0
print(10 ** 2)  #

'''
첫 번째 경우, 11 % -5 = -4나머지는 음수여야 하므로 10과 11이 아니라 15와 11을 비교해야 합니다 11 = (-5) * (-3) + (-4). 
두 번째 경우 , -11 % 5 = 4나머지는 양수여야 합니다. -11 = 5 * (-3) + 4.
'''
print(-11 % 5)    # 4
print(11 % -5)    # -4


EVEREST_HEIGHT = 8848  # 상수 변수
mountain_name = "Everest"  # 파이썬 변수 명명법 : GNU Naming Convention