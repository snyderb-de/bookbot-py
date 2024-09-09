def main():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
    
    char_count = count_characters(file_contents)
    
    sorted_char_count = sort_dict_by_value(char_count)
    
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


def sort_dict_by_value(d):
    # Convert the dictionary into tuples
    items = list(d.items())
    
    # Sort the list by the count of characters
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j][1] < items[j + 1][1]:
                # Swap the elements if the current value is less than the next value
                items[j], items[j + 1] = items[j + 1], items[j]
    
    return items


if __name__ == "__main__":
    main()

