import matplotlib
import numpy as np

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def plot_data(data, mag, clean, cleanData,dataPeaks, peakTime):
    plt.title('Clean 2 Number of Steps')
    # plt.plot([row[0] for row in data],[row[1] for row in data], label="x")
    # plt.plot([row[0] for row in data],[row[2] for row in data], label="y")
    # plt.plot(,[row[3] for row in data], label="z")
    plt.plot([row[0] for row in data], mag, label="mag",color ='y')
    plt.plot(cleanData, clean, label="average")
    plt.plot(peakTime, dataPeaks, "x", color="r")

    plt.legend(loc='upper right')
    plt.show()

# plot_data("test.csv")
