import sys

# sys.stdin.readline()

n1 = int(sys.stdin.readline())
print("sys.stdin :", n1)
n2 = input()
print("input :", n2)

arr = sys.stdin.readline().split()
print("sys.stdin.readline().split() :", arr)
arr = list(map(int, sys.stdin.readline().split()))
print("sys.stdin.readline().split() -> map int :", arr)

