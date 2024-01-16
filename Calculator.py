nr1 = int(input("Chose your first number: "))
nr2 = int(input("Chose your second number: "))
op = ['+','-','/','*']
calc = input("Chose an operation\n+\n-\n/\n*\n")
if(calc == op[0]):
    print(nr1+nr2)
elif calc == op[1]:
    print(nr1-nr2)
elif calc == op[2]:
    print(nr1/nr2)
else:
    print(nr1*nr2)