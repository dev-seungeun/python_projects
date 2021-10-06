import random

passlen = int(input("enter the length of password : "))
s = "abcdefghijkhmnopqrstuwxyz01234567890ABCDEFGHIJKLMNOPQRSTUWXYZ!@#$%^&*"
p = "".join(random.sample(s, passlen))
print(p)
