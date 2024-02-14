import re
import sys


def main():
    print(parse(input("HTML: ")))
def parse(s):
    n = re.search(r'.+src="https?://(?:www.)?youtube.com/embed/(.+)"',s)
    if n:
        t = "https://youtu.be/" + n.group(1)
        return t
if __name__ == "__main__":
    main()
