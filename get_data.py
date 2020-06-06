""" 这部分获取全书信息 """

# import collections
import re

def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese
    # print(chinese)


def add_comma(text):
    added_text = ''
    for word in text:
        added_text += word + ','
    return added_text


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

book_text = str(find_chinese(book_text))
comma_text = add_comma(book_text)
# print(book_text[19800:20000])

# print(len(book_text))
# print(book_text[5800:6000])
# text = "你知道啥玩意儿"
# word_set = set(book_text)
# print(word_set)

""" count character frequency (non-space) """
word_exception = ['‘']
frequency = {} #-- 汉字出现频率
# word_set = [] #-- 汉字集合
# word_list = []
for word in book_text:
    if word not in word_exception:
        # word_list.append(word)
        if word not in frequency:
            frequency[word] = 1
            # word_set.append(word)
        else:
            frequency[word] += 1
# print(frequency['走'])
# print(len(frequency))
# print(word_set[200:250])
cnt = 0
for word, times in frequency.items():
    if times > 10:
        # print(word)
        cnt += 1
print(cnt)

""" count how many times a name appears """
name_string = ''
appear_times = {} #-- 人名出现次数
for name in names:
    appear_times[name] = book_text.count(name)
    name_string += (name + ',') * appear_times[name]


# print(name_string[:200])
# for name, times in appear_times.items():
#     print(name + ' appears ' + str(times) + ' times.')
# print(name_string[10000:10200])
# print('----')