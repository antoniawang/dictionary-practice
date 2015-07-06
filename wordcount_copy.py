# put your code here
open_file = open("test.txt")
file_dict = {}

def word_count(open_file):
    for line in open_file:
        line = line.rstrip()
        words = line.split(' ')


"""
    if the word is NOT in file_dict:
        assign to value to 1
    else: #if the word is already in the current dictionary
        increase value by 1
"""
        for word in words:
            i = 1
            file_dict[word] = i
            i += 1
    print file_dict

word_count(open_file)