def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    num_words = get_num_words(text)
    print(f"{num_words} words are in this text.")
    get_char_count(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["count"]

def get_char_count(text):
    lower_text = text.lower()
    char_count_dict = {}
    for i in lower_text:
        if i.isalpha():
            if not i in char_count_dict:
                char_count_dict[i] = 1
                #print(f"Adding {i} to char_counts")
            else:
                char_count_dict[i] += 1
    
    #print(char_count_dict)

    char_count_list = []
    for char in char_count_dict:
        char_dict = {}
        char_dict["letter"] = char
        char_dict["count"] = char_count_dict[char]
        char_count_list.append(char_dict)
    
    char_count_list.sort(reverse=True, key=sort_on)
    #print(char_count_list)
    for char_count in char_count_list:
        print(f"The '{char_count["letter"]}' character was found {char_count["count"]} times")



main()
