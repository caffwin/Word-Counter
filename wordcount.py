# put your code here.
file_name = open("test.txt")

def words_count(file_name):

    counts = {}

    for line in file_name:
        print(line)
        line = line.rstrip()
        print(line)
        words = line.split()

        for word in words:
            word = word.rstrip(",")
            print(word)
            counts[word] = counts.get(word, 0) + 1

    return counts

print(words_count(file_name))
