import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)


def k_means(x, y, center_x, center_y):

    def show():
        for i in range(len(x)):
            if label[i] == 0:
                plt.scatter(x[i], y[i], c='r')
            else:
                plt.scatter(x[i], y[i], c='b')
        plt.scatter(center_x, center_y, c='g')
        plt.show()

    label = []
    for i in range(len(x)):
        d1 = np.sqrt((x[i] - center_x[0]) ** 2 + (y[i] - center_y[0]) ** 2)
        d2 = np.sqrt((x[i] - center_x[1]) ** 2 + (y[i] - center_y[1]) ** 2)
        if d1 < d2:
            label.append(0)
        else:
            label.append(1)
    x0 = []
    y0 = []
    x1 = []
    y1 = []
    for i in range(len(x)):
        if label[i] == 0:
            x0.append(x[i])
            y0.append(y[i])
        else:
            x1.append(x[i])
            y1.append(y[i])
    show()
    return np.mean(x0), np.mean(y0), np.mean(x1), np.mean(y1)


if __name__ == '__main__':
    x = np.random.randn(100)
    y = np.random.randn(100)
    center_x = np.random.uniform(-3, 3, 2)
    center_y = np.random.uniform(-3, 3, 2)
    for _ in range(6):
        if _ == 0:
            x0, y0, x1, y1 = k_means(x, y, center_x, center_y)
        else:
            x0, y0, x1, y1 = k_means(x, y, [x0, x1], [y0, y1])
