import matplotlib.pyplot as plt
marks = [55, 60, 71, 63, 55, 65, 50, 55, 58, 59,
         61, 63, 65, 67, 71, 72, 75]
marks.sort()
print("Sorted Marks:")
print(marks)
num_bins = 3
bin_size = len(marks) // num_bins
equal_frequency = []
for i in range(0, len(marks), bin_size):
    equal_frequency.append(marks[i:i + bin_size])
print("\nEqual-Frequency (Equi-Depth) Partitions:")
for i, b in enumerate(equal_frequency, 1):
    print("Bin", i, ":", b)
min_val = min(marks)
max_val = max(marks)
width = (max_val - min_val) / num_bins
equal_width = [[] for _ in range(num_bins)]
for value in marks:
    index = int((value - min_val) / width)
    if index == num_bins:
        index -= 1
    equal_width[index].append(value)
print("\nEqual-Width Partitions:")
for i, b in enumerate(equal_width, 1):
    print("Bin", i, ":", b)
plt.hist(marks, bins=3, edgecolor='black')
plt.title("Histogram of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
