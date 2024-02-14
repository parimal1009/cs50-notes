a = input("camelCase: ")
b = False
for i in a:
    if i.isupper():
        b = True
        if b==True:
            c = a.index(i)
            a = a[:c]+'_'+a[c:]
            a = a.lower()
print("snake_case:",a)
