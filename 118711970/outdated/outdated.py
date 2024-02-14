b = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    a = input("Date: ")
    if "/" in a:
        c,d,e = a.split('/')
    elif "," in a:
        a = a.replace(',','')
        c,d,e = a.split(' ')
        if c in b:
            c = b.index(c) + 1
    try:
        if int(c) > 12 or int(d)>31:
            continue
        else:
            break
    except ValueError:
        continue
print(f"{int(e):02}" + '-' + f"{int(c):02}" + '-' + f"{int(d):02}",end = '',sep = '')
