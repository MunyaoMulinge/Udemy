numb1 = int(input("Enter the first number:\n"))
numb2 = int(input("Enter the second number:\n"))
signs = input("Enter sign:\n")
if signs == "+":
    print(numb1+numb2)
elif signs == "-":
    print(numb1-numb2)
elif signs == "*":
    print(numb1*numb2)
elif signs == "/":
    print(numb1/numb2)
else:
    print("Invalid Operand")