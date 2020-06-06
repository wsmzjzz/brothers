""" 这部分主管绘图 """

#-- 导入处理好的数据
from get_data import book_text, comma_text, name_string
# from get_data import appear_times, frequency
#-- 导入绘图库
import math
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
# import jieba

# print(space_text[:100])
# print(book_text[:100])
# print(list(word_list)[:100])
# print(name_string[:200])
# print('-------')

plt.figure(figsize = (10, 6))

c_font = '/System/Library/Fonts/PingFang.ttc'
#-- 一百单八将名字词云
name_cloud = WordCloud(collocations=False,background_color="white",
                        width=1000, height=860,
                        font_path=c_font, margin=2).generate(name_string)
plt.subplot(121)
plt.imshow(name_cloud)
plt.axis("off")
# plt.show()
#-- 全文汉字单个字词云
word_cloud = WordCloud(collocations=False,background_color="white",
                        width=1000, height=860,regexp=r"\w[\w']*",
                        font_path=c_font, margin=2).generate(comma_text)
plt.subplot(122)
plt.imshow(word_cloud)
plt.axis("off")
plt.show()
