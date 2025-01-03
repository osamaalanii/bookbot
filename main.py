def main():
    path = "books/frankenstein.txt"
    file_content = read_file(path)
    wordes_num =count_words(file_content)
    charecters_num = count_characters(file_content)
    alphabet_char = char_isalpha(charecters_num)
    sorted_char = sorting_function(alphabet_char)
    charecters_report= report(sorted_char,path,wordes_num)


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

def char_isalpha(char_num):
    X={}
    for char in char_num:
        if char.isalpha():
             X[char] = char_num[char]
            

    return X

def sorting_function(dictionary):
    sorted_dic = dict(sorted(dictionary.items(),key= lambda item:item[1],reverse=True))
    return sorted_dic

def report(char_num,file_path,num_of_words):
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_of_words} words found in the document")
    for char in char_num:
        print(f"The {char} character was found {char_num[char]} times")
    print("--- End report ---")



main()