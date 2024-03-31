# solution
# https://raw.githubusercontent.com/bootdotdev/courses/main/courses/build-bookbot/1-project/exercises/16-report/complete/main.py?token=AFHZKVK4TJOMFKWRNFJPAALGBF2MW

def sort_on(dict):
    return dict["num"]

def main():
    book_path = 'books/frankenstein.txt'
    book_text = read_book(book_path)
    word_count = count_words(book_text)
    character_c = character_count(book_text)
    character_list = convert_dic_to_list(character_c)
    character_list.sort(reverse=True, key=sort_on)
    print(f"{word_count} words found in the document")
    for i in character_list:
        letter = i['char']
        number = i['num']
        print(f"the '{letter}' character was found {number} times")
        


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

def convert_dic_to_list(the_dic):
    # char_dic = {'a': 12, 'c':10}
    char_list = []
    for key, value in the_dic.items():
        char_list.append({'char': key, 'num': value})
    return char_list
        

def read_book(path):
    with open(path) as f:
        return f.read()


# character_count()
main()
# convert_dic_to_list()
