def word_counter(text):
    words = text.split()
    return len(words)

def main():
    text = input("enter some text:")
    print("word count:",word_counter(text))

main()