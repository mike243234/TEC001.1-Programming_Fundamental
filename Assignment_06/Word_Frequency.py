
def word_frequency(text):
    words = text.split()
    count = {}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count


sentence = input("Enter a sentence: ")
result = word_frequency(sentence)

for word in result:
    print(word, ":", result[word])
