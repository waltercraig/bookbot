def main():
    book_path = 'books/frankenstein.txt'
    book_text = read_book(book_path)
    word_count = count_words(book_text)
    character_c = character_count(book_text)
    # print(f"{word_count} words found in the document")
    # for i in len(character_c):
    #     print(character_c[i])
    # print(character_c)
    print(len(character_c))

def count_words(string):
    # split the string
    split_string = string.split()
    # get the length of the array
    return len(split_string)

def character_count(string):
    character_list = {}
    for i in string:
        if i != ' ':
            x = i.lower()
            if x not in character_list:
                character_list[x] = 1
            else:
                character_list[x] += 1
    return character_list

def read_book(path):
    with open(path) as f:
        return f.read()


# character_count()
main()
