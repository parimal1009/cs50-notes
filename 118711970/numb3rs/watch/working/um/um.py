import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    t = re.findall(r"\b(um|Um)\b",s)
    return len(t)

if __name__ == "__main__":
    main()
