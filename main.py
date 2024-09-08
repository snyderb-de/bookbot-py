def main():

    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"Word Count: {word_count}")

    char_count = count_characters(file_contents)
    print("Character Count", char_count)


def count_characters(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

if __name__ == "__main__":
    main()
