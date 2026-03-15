text = "the cat sat on the mat the cat"
words = text.split()
frequency = {}

for word in words:
    if word in frequency:

        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)