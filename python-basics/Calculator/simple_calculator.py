# Simple Calculator
def calculate(a , op , b):
    if (op == '+'):
        a += b
        return a
    elif (op == '-'):
        a -= b
        return a
    elif (op == '*'):
        a *= b
        return a
    elif (op == '/'):
        if (b == 0):
            return "Error: Division by zero!"
        else:
            a /= b
            return a
    elif (op == '%'):
        a %= b
        return a
    else:
        print("The equation op is invalid! Please try again.")

a = float (input ("Give First number: "))
op = input ("Give operator: ")
b = float(input ("Give Second number: "))

print(calculate(a , op , b))

conti = input ("Do you want to continue? (y/n): ").lower()
while (conti == 'y'):
    op = input ("Give the equation op: ")
    b = float(input ("Give number: "))
    
    print(calculate(a , op , b))

    conti = input ("Do you want to continue? (y/n): ").lower()