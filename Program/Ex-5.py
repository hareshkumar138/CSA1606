import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
age = [23, 23, 27, 27, 39, 41, 47, 49, 50,
       52, 54, 54, 56, 57, 58, 58, 60, 61]
fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2,
       34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
print("Mean of Age =", round(np.mean(age), 2))
print("Mean of %Fat =", round(np.mean(fat), 2))
print("\nMedian of Age =", np.median(age))
print("Median of %Fat =", np.median(fat))
print("\nStandard Deviation of Age =", round(np.std(age, ddof=1), 2))
print("Standard Deviation of %Fat =", round(np.std(fat, ddof=1), 2))
plt.figure(figsize=(8,4))
plt.boxplot([age, fat], labels=["Age", "%Fat"])
plt.title("Boxplots of Age and %Fat")
plt.grid(True)
plt.show()
plt.figure(figsize=(6,4))
plt.scatter(age, fat)
plt.title("Scatter Plot of Age vs %Fat")
plt.xlabel("Age")
plt.ylabel("%Fat")
plt.grid(True)
plt.show()
plt.figure(figsize=(6,4))
stats.probplot(age, dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")
plt.grid(True)
plt.show()
plt.figure(figsize=(6,4))
stats.probplot(fat, dist="norm", plot=plt)
plt.title("Q-Q Plot of %Fat")
plt.grid(True)
plt.show()
