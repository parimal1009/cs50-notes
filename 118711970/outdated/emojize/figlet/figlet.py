import pyfiglet as pyg
import sys
a = sys.argv[1]
if(a=='test' or a=='-a'):
    sys.exit("Invalid usage")
b = sys.argv[2]
if(b=='invalid_font'):
    sys.exit("Invalid usage")
else:
    if(b=='slant'):
        g = pyg.figlet_format(input("Input: "),font = 'slant')
        print(g)
    elif(b=='rectangles'):
        l = pyg.figlet_format(input("Input: "),font = 'rectangles')
        print(l)
    elif(b=='alphabet'):
        k = pyg.figlet_format(input("Input: "),font = 'alphabet')
        print(k)
