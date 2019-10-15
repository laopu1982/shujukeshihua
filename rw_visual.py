import  matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建一个RandomWalk 实列

while True:
    # 多次随机漫步


    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values,rw.y_values,c="red",edgecolors='none',s=15)
    plt.show()

    keep_running = input ("Make another walk? (Y/N):")
    if keep_running == 'n':
        break
