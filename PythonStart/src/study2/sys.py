import sys

# input, print
n2 = input()
print("input :", n2)


# sys.stdin.readline(), sys.stdout.write()
n1 = int(sys.stdin.readline())
sys.stdout.write("sys.stdin : " + str(n1) + '\n')
arr = sys.stdin.readline().split()
sys.stdout.write("sys.stdin.split : " + str(arr) + '\n')


# map(function, iterable), sys.stdout.write()
arr = list(map(int, sys.stdin.readline().split()))
sys.stdout.write("sys.stdin.split -> map int : " + str(arr) + '\n')


# list comprehension, sys.stdout.write()
# list 객체 선언부에서 for 문을 이용하여 객체를 선언
arr = [int(x) for x in sys.stdin.readline().split()]
sys.stdout.write("list comprehension : " + str(arr) + '\n')

arr = [int(x) * 2 + 1 for x in sys.stdin.readline().split()]
sys.stdout.write("list comprehension : " + str(arr) + '\n')

