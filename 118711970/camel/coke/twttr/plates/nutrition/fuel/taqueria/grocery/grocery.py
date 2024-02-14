d = 1
b = []
try:
    while True:
        a = input().upper()
        b.append(a)
except EOFError:
    b.sort()
    for i in range(0,len(b)):
        f = 0
        for j in range(i+1,len(b)):
            if(b[i]==b[j]):
                f = f+1
                d = b.count(b[i])
        if f==0:
            print(f"{d} {b[i]}")
