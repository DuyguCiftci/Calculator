text = """
Simple Calculator
"""
print(text)

function =  """
1-Add
2-Subtract
3-Multiply
4-Devide
5-Power
6-Prime number
7-Factorial
"""
print(function)
function=input("Select the number of function: ")

if function == "1":
    num1 = int(input("Type the first number: "))
    num2 = int(input("Type the second number: "))
    print("Result: ",num1+num2)
elif function == "2":
    num1 = int(input("Type the first number:  "))
    num2 = int(input("Type the second number: "))
    print("Result: ",num1-num2)
elif function == "3":
    num1 = int(input("Type the first number: "))
    num2 = int(input("Type the second number: "))
    print("Result: ",num1*num2)
elif function == "4":
    num1 = int(input("Type the first number: "))
    num2 = int(input("Type the second number: "))
    print("Result: ",num1/num2)
elif function == "5":
    num1 = int(input("Type the first number: "))
    num2 = int(input("Type the second number: "))
    print("Result: ",num1**num2)   
elif function == "6":
    num = int(input("Type the number: "))
    for i in range(2,num):
        if num % i != 0:
            print("This number is prime.")
            break
        else:
            print("This number is not prime.")
            break
elif function == "7":
    num = int(input("Type the number: "))
    result = 1
    for i in range(num,0,-1):
        result = result * i
    print("Result: ", result)
else :
    print("Invalid function")

print("Bye")
    

