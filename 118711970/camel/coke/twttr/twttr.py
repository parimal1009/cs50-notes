vowels = ['a','A','e','E','i','I','o','O','u','U']
a = input("Input: ")
c = a
for ele in a:
    if ele in vowels:
        c = c.replace(ele,'')
print("Output:",c)
