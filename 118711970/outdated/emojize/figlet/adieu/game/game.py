import random
import sys
p = random.randint(1,100)
try:
    while True:
        n = int(input("Level: "))
        if(n <0):
            continue
        else:
            while True:
                g = int(input("Guess: "))
                if(g<0):
                    continue
                else:
                    if(g>p):
                        print("Too large!")
                    elif(g<p):
                        print("Too Small!")
                    else:
                        print("Just right!")
                        sys.exit()
except ValueError:
    while True:
        n = int(input("Level: "))
        if(n <0):
            continue
        else:
            while True:
                g = int(input("Guess: "))
                if(g<0):
                    continue
                else:
                    if(g>p):
                        print("Too large!")
                    elif(g<p):
                        print("Too Small!")
                    else:
                        print("Just right!")
                        sys.exit()
