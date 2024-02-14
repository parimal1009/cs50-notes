import sys
from PIL import Image, ImageOps
if len(sys.argv) == 3:
    if sys.argv[1][-3:] == 'jpg' or sys.argv[1][-3:] =='png' or sys.argv[1][-4:] == 'jpeg':
        if(sys.argv[1][-3:]==sys.argv[2][-3:]):
            try:
                image = Image.open(sys.argv[1])
            except FileNotFoundError:
                sys.exit("File does not exist")
            w = Image.open('shirt.png')
            size = w.size
            image = ImageOps.fit(image, size)
            image.paste(w,w)
            image.save(sys.argv[2])
        elif(sys.argv[1][-3:]!= sys.argv[2][-3:]):
            sys.exit("Input and output have different extensions")r
    elif(sys.argv[2][-3:]!='jpg'):
        sys.exit("Invalid output")
    elif(sys.argv[1]!= 'before1.jpg' or sys.argv[1]!= 'before2.jpg'or sys.argv[1]!= 'before3.jpg'):
        sys.exit("Input does not exist")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
