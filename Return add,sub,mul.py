def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

for i in range(2):
    print("Addition:", add(a, b))
    print("Subtraction:", sub(a, b))
    print("Multiplication:", mul(a, b))
