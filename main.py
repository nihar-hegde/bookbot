from stats import count_wrords, sort_dir, no_of_charecters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_file_path):
    with open(book_file_path) as file:
        book_text = file.read()
    return book_text


def main():
    book_file_path = sys.argv[1]
    book_text = get_book_text(book_file_path)
    count_words = count_wrords(book_text)
    # print(f"Found {count_words} total words")
    char_dict = no_of_charecters(book_text)
    sorted_char_dict = sort_dir(char_dict)
    for char in sorted_char_dict:
        if char.isalpha():
            print(f"{char}: {sorted_char_dict[char]}")

main()