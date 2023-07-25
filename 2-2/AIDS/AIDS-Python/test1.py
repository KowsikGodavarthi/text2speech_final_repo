print("calculator")
for i in range(0,10):
    print("1. Addition\n2. Subraction\n3. Multiplication\n4. Division\n")
    print("enter your choice\n")
    choice=input("enter here\n")
    choic  = int(choice)    
    if choic == 1:
        print("enter the two numbers\n")
        x=input()
        y=input()
        c=int(x)+int(y)
        print(c)
    elif choic == 2:
        print("enter the two numbers\n")
        x=input()
        y=input()
        c=int(x)-int(y)
        print(c)
    elif choic == 3:
        print("enter the two numbers\n")
        x=input()
        y=input()
        c=int(x)*int(y)
        print(c)
    elif choic == 4:
        print("enter the two numbers\n")
        x=input()
        y=input()
        c=int(x)/int(y)
        print(c)
    else:
        print("invalid input")
        break    
