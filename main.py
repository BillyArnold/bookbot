def character_count(text):
    alphabet_dict = {}
    lowered_text = text.lower()

    for letter in lowered_text:
        if letter in alphabet_dict and letter.isalpha():
            alphabet_dict[letter] += 1
        elif letter.isalpha():
            alphabet_dict[letter] = 1
    
    return alphabet_dict

def get_book_text(book_name):
    with open(f"books/{book_name}.txt") as f:
        file_contents = f.read()
    
    return file_contents

def get_word_count(text):
    words = text.split()
    return len(words)

def print_report(word_count, letter_counts, book_name):
    print(f"--- Begin report of books/{book_name}.txt ---")
    print(f"Words found: {word_count} \n")

    for letter in letter_counts:
        print(f"The {letter['letter']} count is {letter['num']}")

def sort_on(dict):
    return dict["num"]

def sort_dict_by_num(num_dict):
    #convert to array
    array_to_sort = []
    for character in num_dict:
        array_to_sort.append({
            "letter": character,
            "num": num_dict[character]
        })
    
    array_to_sort.sort(reverse=True, key=sort_on)
    return array_to_sort

def main():
    book_name = "frankenstein"
    book_text = get_book_text(book_name)
    word_count = get_word_count(book_text)
    letter_counts = character_count(book_text)
    letters_in_order = sort_dict_by_num(letter_counts)

    print_report(word_count, letters_in_order, book_name)
    print('finished')

main()