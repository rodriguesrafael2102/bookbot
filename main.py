def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_words = count_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_words} words found in the document")
    print()

    character_dictio = get_count_character(text)
    sorted_list = dictio_into_sorted_list(character_dictio)
    
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"The {item["char"]} character was found {item["num"]} times")

    print(f"--- End report ---")


def sort_on(d):
    return d["num"]

def dictio_into_sorted_list(dictio):
    sorted_list = []
    for ch in dictio:
        sorted_list.append({"char": ch, "num": dictio[ch]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_dict(dictio):
    return dictio["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    list_words = text.split()
    number_words = len(list_words)
    return number_words

def get_count_character(text):
    char_dict = {}
    lowered_text = text.lower()
    for char_in_text in lowered_text:
        if char_in_text in char_dict:
            char_dict[char_in_text] += 1
        else:
            char_dict[char_in_text] = 1
        
    return char_dict

main()