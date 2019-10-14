# -*-coding:utf-8-*
import matplotlib.pyplot as plt


plt.scatter(2,4,s=300)

# 设置图表标题并给坐标轴加标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置个刻度标记的大小
plt.tick_params(axis="both" , which="major" , labelsize=10)

plt.show()