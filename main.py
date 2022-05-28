# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
     with open(filename, 'r') as file:
       file_content = file.read()
       return file_content

def count_words():
     import re
     text = read_file_content("./story.txt")
     text = text.lower()
     text = re.sub(r'[^\w]', ' ', text)
     text = re.sub(' +', ' ', text)
     textwords = text.split(" ")
     dictWords = {}
     for word in textwords:
       if word in dictWords.keys():
            dictWords[word] += 1
       elif word == "":
            pass
       else:
            dictWords[word] = 1
     print(dictWords)
     return dictWords
count_words()
