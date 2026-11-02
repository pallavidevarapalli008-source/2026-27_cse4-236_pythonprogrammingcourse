number=int(input("Enter an integer:"))
if number>0:
    if number %2==0:
        print(f"{number} is positive and even")
    else:
        print(f"{number} is positive and odd")
elif number<0:
        print(f"{number} is negative")
else:
    print(f"{number} is zero")

