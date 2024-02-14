x = input("File name: ").strip().lower()
d = '.'
p = x.rfind(d)
if(x[-2]=='i'):
    if(x[-1]=='f'):
        print("image/gif")
    elif(x[-1]=='p'):
        print("application/zip")
    else:
        print("application/octet-stream")
elif(x[-2]=='p'):
    print("image/jpeg")
elif(x[-2]=='e'):
    print("image/jpeg")
elif(x[-2]=='n'):
    print("image/png")
elif(x[-2]=='d'):
    print("application/pdf")
elif(x[-2]=='x'):
    print("text/plain")
else:
    print("application/octet-stream")
