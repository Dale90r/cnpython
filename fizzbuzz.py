num = 35

if num %3 == 0 and num %5 == 0:
    print("number is devisible by 3 and 5")
    print("fizzbuzz")
    print(num)
elif num %3 ==0:
    print("buzz divisible by 3")
    print(num)
elif num %5 ==0:
    print("buzz divisible by 5")
    print(num)
else:
    print("number is not devisible by 3 or 5")
    print("fizz")
    print(num)