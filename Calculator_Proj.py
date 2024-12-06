def addop(x,y):
    return x + y

def subop(x,y):
    return x - y

def multop(x,y):
    return x * y

def divop(x,y):
    return x / y

b = True

while b:

    x = float(input("please enter your first number: "))
    y = float(input("please enter your second number: "))
    op = str(input("please enter your operation "))

    if op == "add": print(addop(x,y))
    elif op == "sub": print(subop(x,y))
    elif op == "mult": print(multop(x,y))
    elif op == "div": print(divop(x,y))
    else: print('invalid input')

    continues = input("Do you want to continue? yes or stop")

    if continues == "yes": b=b
    elif continues == "stop": b = False
    else: print('invalid input')