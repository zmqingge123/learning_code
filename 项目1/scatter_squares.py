from re import X
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("_classic_test_patch")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#设置图标标题并给坐标轴加上标签。
ax.set_title("square", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("value of square", fontsize=14)

#s设置刻度标记的大小。
ax.tick_params(axis="both", which="major", labelsize=14)

#设置每个坐标轴的取值范围。
ax.axis([0, 1100, 0, 1100000])

plt.savefig("squares_plot.jpg", bbox_inches="tight")
