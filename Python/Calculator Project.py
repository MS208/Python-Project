def add(x,y):
    return x+y

def subtraction (x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y!=0:
        return x/y

    else:
        return "Cannot divide by zero!"

def calculator():
    print("Basic Calculator")
    print("select Operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice =input ("Enter choice (1/2/3/4):")

    if choice in [ '1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return

        if choice == '1':
            print("Result:", add(num1,num2))
        elif choice == '2':
            print("Result:", subtract(num1,num2))
        elif chouce == '3':
            print("Result:", multiply(num1,num2))
        elif choice == '4':
            print("Result:", divide(num1,num2))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    calculator()
        
