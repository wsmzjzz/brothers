""" 这部分主管绘图 """

#-- 导入处理好的数据
from get_data import names, word_set, book_text
from get_data import appear_times, frequency
#-- 导入绘图库
import math
import matplotlib.pyplot as plt
import numpy as np


# input_1 = np.arange(0 ,math.pi * 2, 0.1)
# input_1 = np.linspace(0 ,math.pi * 2, 50)
# y1 = np.sin(input_1)

# plt.plot(input_1, y1, label='y=sinx')
# squares = [math.log(i) for i in range(2, 50)]
# squares2 = [math.log10(i) for i in range(1, 10)]
# plt.plot(input_1, squares, linewidth=5)
# plt.plot(names, appear_times.values(), linewidth=2, label='y=logx')
# for i in range(len(input_1)):
# plt.scatter(input_1, squares, edgecolors='red')
# x = np.random.normal(0,1,1000)
# y = np.random.normal(0,1,1000)
# t = np.arctan2(y,x)
# plt.scatter(x,y, c=t)

# print(appear_times['宋江'])

for name, times in appear_times.items():
    plt.scatter(name, times)

# plt.legend(loc='upper right')
# plt.title('Logistic Curve', fontsize=20)
# plt.xlabel('x-Axis')
# plt.ylabel('y=log(x)')
# plt.tick_params(axis='x', labelsize=10)
plt.show()
