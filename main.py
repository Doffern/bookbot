import sys

from stats import word_count, char_counts_sorted, char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    # Relativ path fra main.py til frankenstein.txt
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    num_words = word_count(book_text)
    char_counts_amount = char_counts(book_text)
    sort_char_counts_amount = char_counts_sorted(char_counts_amount)
    
    #print(char_counts_amount)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sort_char_counts_amount:
        print(f"{char}: {count}")
    print("============= END ===============")

main()