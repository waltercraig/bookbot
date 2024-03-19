def main():
    book_path = 'books/frankenstein.txt'
    book_text = read_book(book_path)
    print(book_text)


def read_book(path):
    with open(path) as f:
        return f.read()

main()
