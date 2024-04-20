
from english_words import get_english_words_set
from pprint import pprint

def letters_to_binary(string,important):
    bin_array = [0]*26
    important_ascii = ord(important) - 97
    important_i = 0
    for char in string: 
        index = ord(char) - 97
        if index >= 0 and index <= 25 and bin_array[index] == 0 :
            bin_array[index] = 1
            if index == important_ascii:
                important_i = index
    tup = tuple(bin_array)
  
    return tup,important_i

    
def find_all_words(bin_tup, index, words):
    total_words = []
    for word in words:
        if len(word) < 4: 
            continue

        temp, blah = letters_to_binary(word, 'a')
        flag = True 

        for i in range(len(bin_tup)): 
            if temp[index] != 1 or temp[i] == 1 and bin_tup[i] == 0:
                flag = False
                break 
        if flag: 
            total_words.append(word)  
    return total_words


if __name__ == "__main__":
    #enter the letters of the day here, you can modify the string
    letters_of_day = "oktilnb"
    #enter the important letter here 
    important_letter = 'b'
    words = get_english_words_set(['web2'], lower=True)

    letter_tuple,letter_index = letters_to_binary(letters_of_day, important_letter)
    letters_words = find_all_words(letter_tuple, letter_index, words)
    pprint(letters_words)


