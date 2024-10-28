def addition(a,b):
    p=a+b
    return p
def subtraction(a,b):
    q=a-b
    return q
def multiplication(a,b):
    r=a*b
    return r
def division(a,b):
    s=a/b
    return s
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
print('''MENU
1) Addition
2)Subtraction
3)Multiplication
4)Division''')
n=int(input("Enter your choice:"))

if n==1:
    result_of_addition=addition(n1,n2)
    print("addition: ",result_of_addition)
elif n==2:
    result_of_subtraction=subtraction(n1,n2)
    print("subtraction: ",result_of_subtraction)
elif n==3:
    result_of_mutiplication=multiplication(n1,n2)
    print("multiplication: ",result_of_mutiplication)
elif n==4:
    result_of_division=division(n1,n2)
    print("division: ",result_of_division)
else:
    print("You have entered the wrong choice")

