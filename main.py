from stats import get_num_words, get_char_frequency, format_frequencies
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    content = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(content)} total words")
    print("--------- Character Count -------")
    char_count = format_frequencies(get_char_frequency(content))
    for cc in char_count:
        if cc['char'].isalpha():
            print(f"{cc['char']}: {cc['num']}")
    print("============= END ===============")

main()