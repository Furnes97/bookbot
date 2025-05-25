
def word_count(text):
    #counter = 0
    #for word in text.split():
    #    counter += 1
    words = text.split()
    return len(words)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_char_count(text):
    dic = {}
    for character in text:
        lowered = character.lower()
        if lowered in dic:
            dic[lowered] += 1
        else:
            dic[lowered] = 1
    return dic


def get_report_dic(dictionary):
    def sort_on(dict):
        return dict["num"]
    dic_keys = dictionary.keys()
    ls = []
    for key in dic_keys:
        ls.append({"char":key, "num":dictionary[key]})

    #ls_sorted = ls.sort(key=sort_on, reverse=True)
    #for i in ls_sorted:
    #    if i["char"].isalpha():
    #        print(f"{i["char"]}: {i["num"]}")
    #a = [x for x in ls_sorted if x["char"].isalpha()]
    #return ls.sort(key=sort_on, reverse=True)
    ls.sort(reverse=True, key=sort_on)
    return ls



a = get_book_text("books/frankenstein.txt")
b = get_char_count(a)
get_report_dic(b)
