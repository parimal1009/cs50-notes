import inflect
p = inflect.engine()
try:
    c = []
    while True:
        a = input("Name: ")
        c.append(a)

except EOFError:
    f = p.join(c)
    print(f"Adieu, adieu, to {f}")
