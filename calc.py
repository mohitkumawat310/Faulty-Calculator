oper = input("Please Choose a Operator (+,-,*,/) : \n")
num1 = int(input("Please Enter No. 1 : \n"))
num2 = int(input("Please Enter No. 2 : \n"))
if oper == "+":
    if num1 == 56 and num2 == 9:
        print("Sum Of Your Numbers is : 77")
    else:
        print("Sum Of Your Numbers is : ", num1 + num2)
elif oper == "-":
    print("Minus Of Your Numbers is : ", num1 - num2)
elif oper == "*":
    if num1 == 45 and num2 == 3:
        print("Multiple Of Your Numbers is :555")
    else:
        print("Sum Of Your Numbers is : ", num1 * num2)
elif oper == "/":
    if num1 == 56 and num2 == 6:
        print("Devide Of Your Numbers is : 4")
    else:
        print("Sum Of Your Numbers is : ", num1 / num2)
else:
    print("Invaild Operator")
