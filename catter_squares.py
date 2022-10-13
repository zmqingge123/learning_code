import matplotlib.pyplot as plt

plt.style.use("_classic_test_patch")
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

#设置图标标题并给坐标轴加上标签。
ax.set_title("square", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("value of square", fontsize=14)

#s设置刻度标记的大小。
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
