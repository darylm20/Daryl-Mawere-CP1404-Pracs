different_words = {}

sentence = input("Sentence: ")

words = sentence.split()
for word in words:
    frequency = different_words.get(word, 0)
    different_words[word] = frequency + 1

words = list(different_words.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
        print ("{:{}} : {}".format(word, max_length, different_words[word]))