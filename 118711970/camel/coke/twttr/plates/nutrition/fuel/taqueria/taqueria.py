d = 0
b = {
        "Baja Taco": 4.00,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }

while True:
    try:
        a = input("Item: ")
    except (ValueError,EOFError):
        print()
        break
    if a in b:
        d = d + b[a]
        print(f"Total: ${d:.2f}" , sep = '')
