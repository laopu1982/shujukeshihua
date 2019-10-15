# -*-coding:utf-8-*
import matplotlib.pyplot as plt


# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
x_values= list(range(1,100))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c='red',edgecolors='none',s=40)

# 设置图表标题并给坐标轴加标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置个刻度标记的大小
plt.tick_params(axis="both" , which="major" , labelsize=10)
plt.axis([0,110,0,11000])

# plt.show()

# 自动保存图表
plt.savefig('squares_plot.png',bbox_inches='tight')