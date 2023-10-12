# fizzbuzz if it is a multiple of 20
# if it is multiple of 4 print fizz
#                      5       buzz


for n in range(1,101):
    if n%20==0:
        print("fizzbuzz")
    elif n%4==0:
        print("fizz")
    elif n%5==0:
        print("buzz")
        