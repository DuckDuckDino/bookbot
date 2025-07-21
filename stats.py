def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def word_count(filepath):
    book = (get_book_text(filepath))
    word_split = book.split()
    count = len(word_split)
    return count

def letter_count(filepath):
    words = (get_book_text(filepath).lower())
    letter_count = {}
    for character in words:
        if character in letter_count:
            letter_count[character] += 1
        else: letter_count[character] =1
    return letter_count

def sort_by_num(item):
    return item["num"]
        
def letter_sort(filepath):
    letters = letter_count(filepath)
    char_sort = [] 
    for char in letters:
         if char.isalpha():
            count = letters[char]
            char_sort.append({"char" :char, "num": count})
    char_sort.sort(reverse=True, key=sort_by_num)
    return char_sort