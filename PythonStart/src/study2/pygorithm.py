import sys

"""
input() 함수와 기능이 똑같다. 
여기서 알아 두면 좋은 것은
sys.stdin은 file 객체와 사용 방법이 같다. 
단지 입력을 인터프리터 내에서 받냐, 파일에서 받냐가 다를 뿐이다.
"""
n1 = int(sys.stdin.readline())
print("sys.stdin :", n1)
n2 = input()
print("input :", n2)
