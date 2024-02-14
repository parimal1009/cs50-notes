import emoji

inp: str = input("Input: ")

emojized: str = emoji.emojize(inp, language='alias')

print(emojized)
