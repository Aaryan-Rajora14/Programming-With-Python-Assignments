# 7. Write a program that reads a file named text.txt and prints a dictionary with words as keys and their frequencies as values.

def count_word_frequencies(filename):
    word_freq = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;:"()[]{}')
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
    return word_freq

filename = 'text.txt'
word_frequencies = count_word_frequencies(filename)
print(word_frequencies)
