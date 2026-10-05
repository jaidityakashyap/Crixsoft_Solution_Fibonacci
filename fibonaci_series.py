def fibonaci_series(n):
    a = 0
    b = 1

    for i in range(n):
        print(a,end=" ")
        a,b = b,a+b


print("Fibnoci Generator")
n = int(input("Enter your value for fibonaci series: "))

if n > 0:
    print("Your desired fibonaci series is :")
    fibonaci_series(n)
    print()
    


else:
    print("Enter a valid value")
    print("Only positive whole numbers can be taken as input.")
