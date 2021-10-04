'''
파이썬은 인터프리터 언어입니다. 실행 전에 소스 코드를 바이트 코드로 컴파일합니다. Python 프로그램을 실행한다는 것은 컴파일과 해석을 모두 의미합니다 .
프로그램이 바이트 코드로 바뀌면 PVM에 의해 한 줄씩 실행 됩니다. 이것이 Python이 C++ 또는 C와 같은 컴파일된 언어보다 느린 이유입니다.
'''


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


# 파이썬 변수 명명법 : GNU Naming Convention
mountain_name = "Everest"
EVEREST_HEIGHT = 8848  # 상수 변수


# Boolean
bool1 = False  # False
bool2 = 0 or True  # True
bool3 = 0 or False  # False
bool4 = 0 and True  # 0
bool5 = 0.0 and True  # 0.0
bool6 = "" and True  # ""
bool7 = "" or True  # True
print(bool1, bool2, bool3, bool4, bool5, bool6, bool7)

a = True
b = False
c = a and not b
print(a and (not c or b))  # False


# Comparisons & Dictionary & for & if
Anne = {"name": "Anne", "average_grade": 49, "recommended_by_tutor": True, "finished_intro_course": False, "intro_course_grade": 0}
John = {"name": "John", "average_grade": 41, "recommended_by_tutor": False, "finished_intro_course": True, "intro_course_grade": 76}
Frank = {"name": "Frank", "average_grade": 37, "recommended_by_tutor": True, "finished_intro_course": True, "intro_course_grade": 97}
Victoria = {"name": "Victoria", "average_grade": 40, "recommended_by_tutor": True, "finished_intro_course": True, "intro_course_grade": 86}
Mary = {"name": "Mary", "average_grade": 49, "recommended_by_tutor": False, "finished_intro_course": True, "intro_course_grade": 85}
Sam = {"name": "Sam", "average_grade": 33, "recommended_by_tutor": False, "finished_intro_course": True, "intro_course_grade": 51}

People = [Anne, John, Frank, Victoria, Mary, Sam]

for p in People:
    enroll_student = ((p['average_grade'] >= 40 and p['recommended_by_tutor']) or (p['finished_intro_course'] and p['intro_course_grade'] > 85))
    if enroll_student:
        print(p['name'])
print()



# List
name = list('Helen')
print(name)
name = ['Helen']
print(name)
empty_list = list()
print(empty_list)

pet = "cat"
first_char = pet[0]   # 'c'
second_char = pet[1]  # 'a'
third_char = pet[2]   # 't'
print(first_char, second_char, third_char)

colors = ['red', 'green', 'blue']
last_elem = colors[-1]    # 'blue'
second_elem = colors[-2]  # 'green'
first_elem = colors[-3]   # 'red'
print(last_elem, second_elem, first_elem)



# 함수 호출

number = "111"

# 1. finding the length of an object
print(len(number))  # 3

# 2. converting types
integer = int(number)
float_number = float(number)
print(str(float_number))  # "111.0"

# 3. adding and rounding numbers
my_sum = sum((integer, float_number))
print(my_sum)  # 222.0
print(round(my_sum))  # 222

# finding the minimum and the maximum
print(min(integer, float_number))  # 111
print(type(max(integer, float_number, my_sum)))  # <class 'float'>

print(type(print))
print()


# 함수 선언
# 1. Function definition
def multiply(x, y):
    return x * y

# 2. Function calls
a = multiply(3, 5)   # 15
b = multiply(a, 10)  # 150
print(a, b)

# 3. 빈 함수 선언
def lazy_func(param):
    pass

number = 3
result = 1
while number >= 1:
    result *= number
    number -= 1
print(result)



# Else statement
age = 15
print('kid' if age < 20 else 'adult')

least = int(input())
full = int(input())
my = int(input())

if my < least:
    print("Deficiency")
elif my >= full:
    print("Excess")
else:
    print("Normal")


# 입력
name = input("input your name : ")
print("My name is", name)

num1 = float(input("input float number : "))
num2 = float(input("input float number : "))
print("num1 + num2 = ", num1+num2)

print()
cnt = int(input("input integer number : "))
word = input("word : ")
print(word * cnt)

