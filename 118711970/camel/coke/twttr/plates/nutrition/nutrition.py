a = input("Input: ")
b = {
    'apple': 130,
    'Avocado': 50,
    'Banana': 110,
    'Cantalope': 50,
    'Grapefruit': 60,
    'Grapes': 90,
    'Kiwifruit': 90,
    'Sweet Cherries': 100,
    'pear':100
    }
for i in b:
    if a in b:
        print("Calories:",b.get(a))
        break
