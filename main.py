from stats import word_count
from stats import letter_count

def get_book_text(f):
    file_contents = f.read()
    return file_contents

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = get_book_text(f)
        num_words = word_count(file_contents)
        letters = letter_count(file_contents)

    print(f"{num_words} words found in the document")
    print(letters)

main()
