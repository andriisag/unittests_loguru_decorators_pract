import re
a = input("введи рядок: ")

def check(a):
    a = re.sub(r'[^\w]', ' ', a)
    words = a.split()
    print(words)
    return words

check(a)