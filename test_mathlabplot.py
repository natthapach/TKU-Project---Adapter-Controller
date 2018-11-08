import matplotlib.pyplot as plt

f = open("log.csv", "r")
data_set = [[[0], [0], [0]],  # thumb
        [[0], [0], [0]],  # index
        [[0], [0], [0]],  # middle
        [[0], [0], [0]],  # ring
        [[0], [0], [0]],  # little
        [[0], [0], [0]]]  # palm
for line in f :
    data = [[0, 0, 0],  # thumb
        [0, 0, 0],  # index
        [0, 0, 0],  # middle
        [0, 0, 0],  # ring
        [0, 0, 0],  # little
        [0, 0, 0]]  # palm
    data_raw = line.split(",")
    for i in range(6) :
        for j in range(3) :
            d = float(data_raw[i*3 + j])
            if (j == 2 and d != 0) :
                d -= 500

            data_set[i][j].append(d)
f.close()

axs = [0]*6
ax_names = ["Thumb", "Index", "Middle", "Ring", "Little", "Palm"]
for i in range(6) :
    axs[i] = plt.subplot(2, 3, i+1)
    axs[i].set_title(ax_names[i])
    legends = ["x", "y", "z"]
    for j in range(3) :
        l, = axs[i].plot(data_set[i][j])
        l.set_label(legends[j])
    axs[i].legend()

plt.show()