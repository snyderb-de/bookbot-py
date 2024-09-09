def main():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
    
    char_count = count_characters(file_contents)
    
    sorted_char_count = list(char_count.items())
    sorted_char_count.sort(key=get_value, reverse=True)
    
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


def count_characters(text):
    text = text.lower()

    char_count = {}

    for char in text:
        # Only count alphabetic characters (ignore spaces, punctuation, etc.)
        if char.isalpha():
            # Increment the count of the character in the dictionary
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count


def get_value(item):   
    return item[1]


if __name__ == "__main__":
    main()

