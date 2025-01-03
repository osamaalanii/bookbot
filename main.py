def main():
    path = "books/frankenstein.txt"
    file_content = read_file(path)
    length =count_words(file_content)
    charecters_num = count_characters(file_content)
    print(charecters_num)

def read_file(path):
    with open(path) as f:
        return f.read()
        
        

def count_words(content):
    split_words = content.split()
    return len(split_words)

def count_characters(content):
    content_lower = content.lower()
    charcters_num = {}
    for char in content_lower:
        charcters_num[char] = 0

    for char in content_lower:
        charcters_num[char] = charcters_num[char]+1

    return charcters_num


    

main()