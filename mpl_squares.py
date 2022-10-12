import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig,ax = plt.subplots()
ax.plot(squares, linewidth=3)

#设置图表标题并给坐标轴加上标签。
ax.set_title("square", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("value of square", fontsize=14)

#设置刻度标记的大小。
ax.tick_params(axis="both", labelsize=14)

plt.show()

