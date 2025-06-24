import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words():
    path_to_file = sys.argv[1]
    num_words = len(get_book_text(path_to_file).split())
    return num_words

def get_num_char():
    path_to_file = sys.argv[1]
    num_char = {}
    char_string = get_book_text(path_to_file).lower()
    for char in char_string:
        if char.isalpha():
            if char not in num_char:
                num_char[char] = 1
            else:
                num_char[char] += 1
    return num_char    

def sort_on(items):
    return items["num"]

def get_sorted_char_count():
    num_char = get_num_char()
    char_count = []
    for key, value in num_char.items():
        char_count.append({"char": key, "num": value})
    char_count.sort(reverse=True, key=sort_on)
    return char_count

def print_organized_char_count():
    char_count = get_sorted_char_count()
    for item in char_count:
        print(f"{item['char']}: {item['num']}")



