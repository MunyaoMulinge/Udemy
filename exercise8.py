pwd = input("Enter your password\n")
if pwd.isalnum():
    print(True)
    if len(pwd) > 6:
        print("Cant accept")
else:
    print(False)
