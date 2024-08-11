def count(book):
    return len(book.split())

def count_char(book):
    book = book.lower()
    res = {}
    for ch in book:
        if not ch in res:
            res[ch] = 1
        else:
            res[ch]+=1
    return res

def report(book):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count(book)} words found in the document")
    char_dict = count_char(book)
    sorted_dict = sorted(char_dict.items(), reverse=True, key= lambda x: x[1])
    for di in sorted_dict:
        if di[0].isalpha():
            print(f"The {di[0]} character was found {di[1]} times")
    print("--- End report ---")
    

def main():
    with open("./books/frankenstein.txt") as f:
        file_content = f.read()
        report(file_content)
        
main()