

a = int(input("введи число: "))

def check(a):
  is_prime = False
  if a == 1:
     print("не просте")
     return is_prime
  elif a > 1:
    for i in range(2, a):
        if (a % i) == 0:
            is_prime = True
            break
    if is_prime:
        print("не просте")
        return is_prime
    else:
        print("просте")
        return is_prime

check(a)