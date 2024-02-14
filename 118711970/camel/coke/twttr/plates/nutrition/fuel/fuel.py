def main():
    a = input("Fraction: ")
    b = convert(a)
    print(gauge(b))
def convert(fraction):
    while True:
        i = fraction.find('/')
        try:
            a = int(fraction[:i])
            b = int(fraction[i+1:])
            z = a/b
            if a>b:
                fraction = input("Fraction: ")
                continue
            else:
                percentage = int(z * 100)
                return percentage
        except (ValueError, ZeroDivisionError):
            continue
def gauge(percentage):
    if percentage>=99:
       return "F"
    elif percentage<=1:
        return "E"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
