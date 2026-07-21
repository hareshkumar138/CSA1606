import numpy as np
speed = [78.3, 81.8, 82, 74.2, 83.4, 84.5, 82.9, 77.5, 80.9, 70.6]
speed.sort()
Q1 = np.percentile(speed, 25)
Q2 = np.percentile(speed, 50)
Q3 = np.percentile(speed, 75)
IQR = Q3 - Q1
std_dev = np.std(speed, ddof=1)
print("Sorted Data:", speed)
print("Q1 =", round(Q1, 2))
print("Median (Q2) =", round(Q2, 2))
print("Q3 =", round(Q3, 2))
print("Interquartile Range (IQR) =", round(IQR, 2))
print("Standard Deviation =", round(std_dev, 2))
