import math

import scipy
from scipy.signal import find_peaks

from plot_data import plot_data
import parser_data

cleanTime = []


def count_steps(data):
    global cleanTime
    print("Accelerometer data graph")

    cleanMag = moving_average(vector_magnitude(data), 100, data)
    '''
    ADD YOUR CODE HERE. This function counts the number of steps in data and returns the number of steps
    '''
    peaks, _ = find_peaks(cleanMag, distance=50)
    peaks = list(peaks)
    dataPeaks = []
    peakTime = []

    for x in peaks:
        dataPeaks.append(cleanMag[x])
        peakTime.append(data[x][0])

    print(len(dataPeaks))
    plot_data(data, vector_magnitude(data), cleanMag, cleanTime, dataPeaks, peakTime)

    num_steps = len(dataPeaks)

    return num_steps


def vector_magnitude(data):
    magnitude = []

    for x in range(len(data)):
        magnitude.append(math.sqrt((data[x][1] ** 2 + (data[x][2]) ** 2) + (data[x][3] ** 2)))

    return magnitude


def moving_average(data, window, data2):
    global cleanTime
    cleanMag = []
    cleanTime = []
    for x in range(len(data) - window):
        average = 0

        for y in range(window):
            average += data[x + y]

        cleanMag.append(average / window)
        cleanTime.append(data2[x][0])

    return cleanMag


def main():
    # Get data
    file_name = "walking_steps_2_cleaned.csv"  # Change to your file name
    data = parser_data.get_data(file_name)
    number_of_steps = count_steps(data)
    print("Number of steps counted are :{0:d}".format(number_of_steps))


if __name__ == "__main__":
    main()
