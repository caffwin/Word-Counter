# put your code here.
# text_file = open("test.txt")

import sys
def words_count(file_name):

    counts = {}

    with open(file_name) as file1:
        for line in file1:
            # print(line)
            # line = line.rstrip()
            # print(line)
            words = line.split()

            for word in words:
                word = word.lower()
                word = word.rstrip(",. ?")
                # print(word)
                counts[word] = counts.get(word, 0) + 1

            print(word)
            print(words)

        for count, num in counts.items():
            print(count, ": ", num)

        return counts

        

words_count(sys.argv[1])