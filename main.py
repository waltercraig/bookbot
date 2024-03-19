def main():
    book_path = 'books/frankenstein.txt'
    book_text = read_book(book_path)
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")

def count_words(string):
    # split the string
    split_string = string.split()
    # get the length of the array
    return len(split_string)

def read_book(path):
    with open(path) as f:
        return f.read()

main()
