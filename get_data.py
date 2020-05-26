""" 这部分获取全书信息 """

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
# text = "你知道啥玩意儿"
# word_set = set(book_text)
# print(word_set)

""" count character frequency (non-space) """
word_exception = ['，', '。', '：', '“', '”', '？', '！', '.', '?', ',', '!']
frequency = {} #-- 汉字出现频率
word_set = [] #-- 汉字集合
for word in book_text:
    if word not in word_exception:
        if word not in frequency:
            frequency[word] = 1
            word_set.append(word)
        else:
            frequency[word] += 1
# print(frequency['走'])
# print(len(frequency))
# print(word_set[200:250])

""" count how many times a name appears """
appear_times = {} #-- 人名出现次数
for name in names:
    appear_times[name] = book_text.count(name)

# for name, times in appear_times.items():
#     print(name + ' appears ' + str(times) + ' times.')
