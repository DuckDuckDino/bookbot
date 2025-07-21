import sys
from stats import word_count
from stats import letter_sort
from stats import letter_count
def main():

    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        
        num_words = (word_count(filepath))


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    characters = letter_sort(filepath)
    for item in characters:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

    



main()