import sys
if len(sys.argv)==3:
    if(sys.argv[1]=="before.csv"):
        try:
            a = "before.csv"
            m = sys.argv[2]
            b = []
            c = []
            d = []
            f = []
            with open(a,'r') as file_1:
                for i in file_1:
                    b.append(i.rstrip().split(","))
                for j in range(1,len(b)):
                    c.append(b[j][1])
                for k in range(1,len(b)):
                    d.append(b[k][0])
                for l in range(1,len(b)):
                    f.append(b[l][2])
            with open(m,'a') as file:
                c = ''.join(c).split('"')
                d = ''.join(d).split('"')
                d.pop(0)
                q = "first"
                r = "last"
                e = "house"
                file.write(f" {q}, {r}, {e}\n")
                for h in range(0,len(f)):
                    file.write(f"{c[h]} {d[h]}, {f[h]}\n")
        except(FileNotFoundError):
            sys.exit("File does not exist")
    elif(sys.argv[1][-3:]!='csv'):
        sys.exit("Not a csv file")
    elif(sys.argv[1] != "before.csv"):
        sys.exit("Could not read invalid_file.csv")
elif(len(sys.argv)>3):
    sys.exit("Too many command-line arguments")
elif(len(sys.argv)<3):
    sys.exit("Too few command-line arguments")
