import matplotlib.pyplot as plt
x = [4, 1, 5, 7, 10, 2, 50, 25, 90, 36]
y = [12, 5, 13, 19, 31, 7, 153, 72, 275, 110]
plt.scatter(x, y)
plt.title("Scatter Plot of Mobile Phones Sold vs Money")
plt.xlabel("Number of Mobile Phones Sold")
plt.ylabel("Money")
plt.grid(True)
plt.show()
