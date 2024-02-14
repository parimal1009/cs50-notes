x,y,z = input("Expression: ").strip().split()
a = float(x)
b = float(z)
if(y=='+'):
    print(a+b)
elif(y=='-'):
    print(a-b)
elif(y=='/'):
    print(a/b)
elif(y=='*'):
    print(a*b)
