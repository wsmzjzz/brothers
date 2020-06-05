""" 这部分主管绘图 """

#-- 导入处理好的数据
# from get_data import names, book_text, word_exception
from get_data import appear_times, frequency, name_string
#-- 导入绘图库
import math
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
import jieba

# space_text = ''
# for word in book_text:
#     space_text += word + ' '
# jieba_words = []
# word_generator = jieba.cut(book_text)
# for chara in word_generator:
#     if chara not in word_exception:
#         jieba_words.append(chara.strip())
# print(jieba_words[:50])

# print(space_text[:100])
# print(book_text[:100])
# print(list(word_list)[:100])
print(name_string[:200])

c_font = '/System/Library/Fonts/PingFang.ttc'
wordcloud = WordCloud(collocations=False,background_color="white",
                        width=1000, height=860,
                        font_path=c_font, margin=2).generate(name_string)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()


# input_1 = np.arange(0 ,math.pi * 2, 0.1)
# input_1 = np.linspace(0 ,math.pi * 2, 50)
# y1 = np.sin(input_1)

# plt.plot(input_1, y1, label='y=sinx')
# squares = [math.log(i) for i in range(2, 50)]
# squares2 = [math.log10(i) for i in range(1, 10)]
# plt.plot(input_1, squar·es, linewidth=5)
# plt.plot(names, appear_times.values(), linewidth=2, label='y=logx')
# for i in range(len(input_1)):
# plt.scatter(input_1, squares, edgecolors='red')
# x = np.random.normal(0,1,1000)
# y = np.random.normal(0,1,1000)
# t = np.arctan2(y,x)
# plt.scatter(x,y, c=t)

# print(appear_times['宋江'])
# for name, times in appear_times.items():
#     plt.scatter(name, times)
# cnt_over = 0
# cnt_lower = 0
# lim = 20
# for word, times in frequency.items():
#     if times > lim:
#         # plt.scatter(word, times)
#         cnt_over += 1
#     else :
#         cnt_lower += 1
# #     cnt += 1
# #     if cnt > 500:
# #         break
# # print('cnt= ' + str(cnt))

# # plt.legend(loc='upper right')
# # plt.title('Logistic Curve', fontsize=20)
# # plt.xlabel('x-Axis')
# # plt.ylabel('y=log(x)')
# # plt.tick_params(axis='x', labelsize=10)
# # plt.title('All Men Are Brothers')
# # plt.show()

# print(f"{cnt_over} words over{lim}")
# print(f"{cnt_lower} words lower{lim}")
