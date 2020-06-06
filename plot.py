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

# plt.rcParams['font.sans-serif']=['SimHei']
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

plt.figure(figsize=(12, 7))
# fig.tight_layout()
plt.subplots_adjust(wspace=0, hspace=0.2)

c_font = '/System/Library/Fonts/PingFang.ttc'
#-- 一百单八将名字词云
name_cloud = WordCloud(collocations=False, background_color="white",
                       width=1000, height=860, mask=shui_mask,
                       font_path=c_font, margin=2).generate(name_string)
plt.subplot(231)
plt.imshow(name_cloud)
plt.axis("off")
# plt.show()
#-- 全文汉字单个字词云
word_cloud = WordCloud(collocations=False, background_color="white",
                       width=1000, height=860, regexp=r"\w[\w']*",
                       mask=hu_mask,
                       font_path=c_font, margin=2).generate(comma_text)
plt.subplot(234)
plt.imshow(word_cloud)
plt.axis("off")


plt.subplot(232)
sort_times = sorted(appear_times.items(),
                    key=lambda item: item[1], reverse=True)
name_label = ['Others', 'Song Jiang', 'Li Kui', 'Wu Song',
              'Lin Chong', 'Wu Yong', 'DaiZong', 'LuJunyi']
name_value = []
rest_occurence = 0
for name, times in sort_times[7:]:
    rest_occurence += times
name_value.append(rest_occurence)
for name, times in sort_times[:7]:
    name_value.append(times)
# print(name_label)
# print(name_value)
expld = (0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02)
plt.pie(name_value,
        labels=name_label,
        autopct='%3.1f%%',
        startangle=180,
        explode=expld)
plt.axis('equal')

plt.subplot(233)
plt.hist(appear_times.values())
plt.xlabel('Number of Occurrences')
# plt.ylabel('Number of people')

plt.subplot(235)
bar_x = ['0-10', '10-100', '100-1000', '>1000']
bar_y = [1618, 1455,859,146]
plt.bar(bar_x, bar_y,color='rgb')
plt.xlabel('Number of Occurrences')

plt.subplot(236)
plt.text(0.05, 0.6, f"The full text has {len(book_text)} words\n" +
         f"composed of {len(frequency.keys())} characters.\n" +
         f"Only 12 of them appear > 5000 times\n" +
         f"More than 50% appear < 20 times",
         size=15,
         style="italic", weight="light",
         bbox=dict(facecolor="r", alpha=0.2))
plt.axis("off")

plt.show()
