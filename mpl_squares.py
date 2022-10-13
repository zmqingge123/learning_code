import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("Solarize_Light2")
fig,ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#设置图表标题并给坐标轴加上标签。
ax.set_title("square", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("value of square", fontsize=14)

#设置刻度标记的大小。
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()

