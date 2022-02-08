lst = []
for i in range(6):
    lst.append(int(input("Enter 6 number\n")))
s = 0
for i in lst:
    s += i
print("Sum of number in the list "+str(s))
