import matplotlib.pyplot as plt
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks
import numpy as np

#*****************************Writing to File**************************
with open("accelerometer.txt", "r") as filestream:
    with open("answers.txt", "w") as filestreamtwo:
        for line in filestream:
            currentline = line.split(",")
            total = str((float(currentline[0])**2 + float(currentline[1])**2 + float(currentline [2])**2)**-2) + "\n"
            filestreamtwo.write(total)

#**********************************************************************


a = []
b = []
with open("answers.txt", "r") as m:
    for index,line in enumerate(m):
        a.append(index)
        b.append(line)


b = list(map(lambda s: s.strip(), b))
map(float, b)
b = [float(i) for i in b]
b = [i*100000 for i in b]
b = [int(float(i)) for i in b]


x = electrocardiogram()[b]
peaks, _ = find_peaks(x, height=-0.17)
print(len(peaks))
plt.plot(x)
plt.plot(peaks, x[peaks], "x")
plt.plot(np.zeros_like(x), "--", color="gray")
plt.show()
