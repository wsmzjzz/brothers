""" Chinese Character Counter """

# import collections

book_path = 'data/book.txt'
names_path = 'data/names.txt'

names = []
with open(names_path, 'r') as name_object:
    """ get all character names """
    for line in name_object:
        names.append(line.strip())
# print(names[:10])
book_text = ''
with open(book_path, 'r') as book_object:
    """ get full text with no space """
    for line in book_object:
        book_text += line.strip()
# print(len(book_text))
# print(book_text[5800:6000])
text = "你知道啥玩意儿"
frequency = {}
# word_set = set(book_text)
# print(word_set)

for word in book_text:
    """ count character frequency (non-space) """
    if word != ' ':
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1
# print(frequency['走'])
print(len(frequency))