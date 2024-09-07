def main():

    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"Word Count: {word_count}")


if __name__ == "__main__":
    main()
