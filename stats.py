import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count():
    entire_book = get_book_text(sys.argv[1])
    num_of_words = entire_book.split()
    return len(num_of_words)

def count_character():
    char_counter = {}
    entire_book = get_book_text(sys.argv[1])
    entire_book = entire_book.lower()
    for c in entire_book:
        if c in char_counter:
            char_counter[c] += 1
        else:
            char_counter[c] = 1
    return char_counter

def sort_on_num(items):
    return items["num"]

def sorted_dict():
    new_counter = count_character()
    # Sort dictionary items by count (value)
    sorted_items = sorted(new_counter.items(), key=lambda x: x[1], reverse=True)
    return sorted_items  
     