import re
a = input("введіть рядок: ")

def check(a):
    a = a.replace(" ", "")
    a = re.sub(r'[^\w]', '', a)
    print(a[::-1])
    if(a == a[::-1]):
        print("паліндром")
        return True
    else:
        print("Не паліндром") 
        return False
check(a)