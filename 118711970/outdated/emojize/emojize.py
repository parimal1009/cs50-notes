import emoji

def emojize_text(text):
    emojized_text = emoji.emojize(text, use_aliases=True)
    return emojized_text

def main():
    user_input = input("Enter text to emojize: ")
    emojized_text = emojize_text(user_input)
    print("Emojized output:", emojized_text)

if __name__ == "__main__":
    main()
