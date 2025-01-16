Num1 = int(input("Enter a Num1 "))
Num2 = int(input("Enter a Num2 "))
Num3 = int(input("Enter a Num3 "))

if Num1 > Num2 and Num1 > Num3:
    print("Max is",Num1)
elif Num2 > Num1 and Num2 > Num3:
    print("Max is ", Num2)
else:
    print("Max is ", Num3)

