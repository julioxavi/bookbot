import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_book_text
from stats import get_num_words
from stats import get_num_char
from stats import sort_on
from stats import get_sorted_char_count
from stats import print_organized_char_count

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words()} total words")
    print("--------- Character Count -------")
    print_organized_char_count()
    print("============= END ===============")

main()


