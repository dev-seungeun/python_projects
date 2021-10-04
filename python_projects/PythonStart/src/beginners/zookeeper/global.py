"""
global VS local
"""

phrase = "Let it be"


def global_printer():
    print(phrase)  # we can use phrase because it's a global variable


global_printer()  # Let it be is printed
print(phrase)  # we can also print it directly

phrase = "Hey Jude"

global_printer()  # Hey Jude is now printed because we changed the value of phrase


def printer():
    local_phrase = "Yesterday"
    print(local_phrase)  # local_phrase is a local variable


printer()  # Yesterday is printed as expected
# print(local_phrase)  # NameError is raised


"""
nonlocal 및 global
"""

x = 1


def global_func():
    global x
    print(x)
    x = x + 1


global_func()  # 1
global_func()  # 2
global_func()  # 3


def func():
    y = 1

    def inner():
        y = 2
        print("inner:", y)

    inner()
    print("outer:", y)


def nonlocal_func():
    y = 1

    def inner():
        nonlocal y
        x = 2
        print("inner:", y)

    inner()
    print("outer:", y)


func()  # inner: 2, outer: 1

nonlocal_func()  # inner: 2, outer: 2
