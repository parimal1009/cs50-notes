import random

def main():
      h = get_level()
      generate_integer(h)

def get_level():
    while True:
        level = input("Level: ")
        if level not in ['1','2','3']:
            continue
        else:
            return level
def generate_integer(level):
    f = 0
    for i in range(10):
        l = 1
        if level==1:
            p = random.randint(100,999)
            g = random.randint(100,999)
        elif level==2:
            p = random.randint(10,99)
            g = random.randint(10,99)
        else:
            p = random.randint(0,9)
            g = random.randint(0,9)
        while True:
            print(f"{p} + {g} =",end = '')
            j = input()
            if j==str(p+g):
                f = f+1
                break
            elif j!=str(p+g) and l !=3:
                print("EEE")
                l = l+1
                continue
            else:
                print("EEE")
                print(f"{p} + {g} = {p + g}")
                break
    print(f"Score: {f}")

if __name__ == "__main__":
    main()
