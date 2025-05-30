from stats import word_count
from stats import letter_count
from stats import list_sort
from stats import sort_on
import sys


def get_book_text(f):
    file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        with open(book_path) as f:
            file_contents = get_book_text(f)
            num_words = word_count(file_contents)
            letters = letter_count(file_contents)
            letter_list = list_sort(letters)
        print_report(book_path, num_words, letter_list)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

def print_report(book_path, num_words, letter_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in letter_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()
