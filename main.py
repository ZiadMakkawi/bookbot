from stats import get_word_count, count_character,sorted_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = get_word_count()
    sorted_chars = sorted_dict()
    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
        # Get sorted characters and print them
    sorted_chars = sorted_dict()
    for char, count in sorted_chars:
        if char.isalpha() and char.isascii():
            print(f"{char}: {count}")
    print("============= END ===============")
    

main()
    