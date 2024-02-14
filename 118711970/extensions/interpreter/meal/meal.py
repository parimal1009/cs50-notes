def main():
    a = input("What time is it? ")
    b = convert(a)
    if(b>=7.00 and b<=8.00):
        print("breakfast time")
    elif(b>=12.00 and b<=13.00):
        print("lunch time")
    elif(b>=18.00 and b<=19.00):
        print("dinner time")

def convert(a):

    hours, minutes = a.split(':')
    hours = float(hours)+(float(minutes)/60)

    return hours

if __name__ == "__main__":
    main()
