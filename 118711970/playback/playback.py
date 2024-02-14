def slowdown_text(input_text):
    slowed_text = '...'.join(input_text.split())
    return slowed_text

user_input = input("Enter a text: ")
output = slowdown_text(user_input)

print("Input with spaces replaced by ...:", output)
