""" 这部分主管绘图 """

#-- 导入处理好的数据
from get_data import book_text, comma_text, name_string
from get_data import appear_times, frequency
#-- 导入绘图库
import math
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator  
from PIL import Image  
# import jieba

plt.rcParams['font.sans-serif']=['SimHei']
# print(space_text[:100])
# print(book_text[:100])
# print(list(word_list)[:100])
# print(name_string[:200])
# print('-------')
shui_path = 'data/shui.png'
shui_mask = np.array(Image.open(shui_path))
shui_color = ImageColorGenerator(shui_mask)
hu_path = 'data/hu.png'
hu_mask = np.array(Image.open(hu_path))
hu_color = ImageColorGenerator(hu_mask)

plt.figure(figsize = (14, 6))

c_font = '/System/Library/Fonts/PingFang.ttc'
#-- 一百单八将名字词云
name_cloud = WordCloud(collocations=False,background_color="white",
                        width=1000, height=860,mask=shui_mask,
                        font_path=c_font, margin=2).generate(name_string)
plt.subplot(231)
plt.imshow(name_cloud)
plt.axis("off")
# plt.show()
#-- 全文汉字单个字词云
word_cloud = WordCloud(collocations=False,background_color="white",
                        width=1000, height=860,regexp=r"\w[\w']*",
                        mask=hu_mask,
                        font_path=c_font, margin=2).generate(comma_text)
plt.subplot(234)
plt.imshow(word_cloud)
plt.axis("off")


plt.subplot(232)
sort_times = sorted(appear_times.items(), key=lambda item:item[1], reverse=True)
name_label = ['Others', 'Song Jiang', 'Li Kui', 'Wu Song', 'Lin Chong', 'Wu Yong', 'DaiZong', 'LuJunyi']
name_value = [400]
for name, times in sort_times[:7]:
    name_value.append(times)
# print(name_label)
# print(name_value)
expld = (0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02)
plt.pie(name_value,
        labels=name_label,
        autopct = '%3.1f%%',
        explode=expld)
plt.axis('equal')

plt.subplot(233)
plt.hist(appear_times.values())
plt.xlabel('Number of Occurrences')
plt.ylabel('Number of people')


plt.show()
