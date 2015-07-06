# put your code here
def word_count(filename):
    open_file = open(filename)
    file_dict = {}

    for line in open_file:
        line = line.rstrip()
        words = line.split(' ')

        for word in words:
            if word not in file_dict:
                file_dict[word] = 1
            else:
                file_dict[word] = file_dict[word] + 1

    for word, number in file_dict.items():
                #print file_dict.get()
        #ey = word
        #value = file_dict[word]
        print "%s %d" %(word, number)
    return file_dict

#word_count("test.txt")
word_count("twain.txt")


"""
    if the word is NOT in file_dict:
        assign to value to 1
    else: #if the word is already in the current dictionary
        increase value by 1
"""