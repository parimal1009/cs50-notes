from datetime import date
import sys
import inflect
i = inflect.engine()
def main():
    try:
        a = input("Date of Birth: ")
        print(ans(a) + " minutes")
    except ValueError:
        sys.exit("Invalid date")
def ans(n1):
    try:
        year,month,day = n1.split("-")
        t = date(int(year),int(month),int(day))
        f = date.today()
        g = int((f-t).total_seconds()/60)
        m = i.number_to_words(g , andword = "")
        return m.capitalize()
    except ValueError:
        return("Invalid Date")
if __name__ == "__main__":
    main()
