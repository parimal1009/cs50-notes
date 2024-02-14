import re
import sys
def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$",s,re.IGNORECASE)
    if match:
        if match.group(2):
            if int(match.group(2))>=60:
                raise ValueError
        elif match.group(5):
            if int(match.group(5))>=60:
                raise ValueError
        num = int(match.group(1))
        if match.group(3) == 'PM' and num != 12:
            num = num + 12
        if match.group(3) == 'AM' and num == 12:
            num = num - 12
        if match.group(2) == None:
            var1 = f"{num:02}:00"
        else:
            var1 = f"{num:02}:{match.group(2)}"
        num_2 = int(match.group(4))
        if match.group(6) == "PM" and num_2 != 12:
            num_2 = num_2 + 12
        elif match.group(6) == "AM" and num_2 == 12:
            num_2 = num_2 - 12
        if match.group(5) == None:
            var2 = f"{num_2:02}:00"
        else:
            var2 = f"{num_2:02}:{match.group(5)}"
        match = f"{var1} to {var2}"
        return match
    else:
        raise ValueError
if __name__ == "__main__":
    main()
