age = eval(input("Enter your age\n"))
if age < 18:
    print("Not eligible to vote.")
    print(f"You will be able to vote after {18-age} years.")
else:
    print("Eligible to vote.")
