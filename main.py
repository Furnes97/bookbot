from stats import word_count, get_char_count, get_report_dic
import sys

def main():
    if len(sys.argv) == 2:
        text = get_book_text(sys.argv[1])
        num_words = word_count(text)
        char_count = get_char_count(text)
        pr_ls = get_report_dic(char_count)
        print("============ BOOKBOT============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in pr_ls:
            if i["char"].isalpha():
                print(f"{i["char"]}: {i["num"]}")
        print("============= END ===============")
        sys.exit(0)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
main()
