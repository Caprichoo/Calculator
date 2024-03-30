def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Pick operation (+,-,*,/)")

def calculate(a,b,operation):
    if operation == '+':
        answer = add(a,b)
    elif operation == '-':
        answer = sub(a,b)
    elif operation == '*':
        answer = mul(a,b)
    elif operation == '/':
        answer = div(a,b)
    return answer

output = calculate(a,b,operation)
print(f"Your answer is {a} {operation} {b} = {output}")

new_operation = input("Pick operation (+,-,*,/)")
new_value = int(input("Enter third number: "))


new_output = calculate(calculate(a,b,operation),new_value,new_operation)
print(f"Your new answer is {output} {operation} {new_value} = {new_output}")



