print("Amount Due: 50")
a = 50
while True:
    b = int(input("Insert Coin: "))
    if(b==25 or b==50 or b==5 or b==10):
        a = a - b
        if(a<50 and a>0):
            print("Amount Due:", a)
            continue
        elif(a<=0):
            a = 50 - (50+a)
            print("Change Owed:", a)
            break
