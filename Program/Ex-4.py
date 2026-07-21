data = [11, 13, 13, 15, 15, 16, 19, 20, 20, 20,
        21, 21, 22, 23, 24, 30, 40, 45, 45, 45,
        71, 72, 73, 75]
bin_size = 3
bins = [data[i:i + bin_size] for i in range(0, len(data), bin_size)]
print("Original Bins:")
for b in bins:
    print(b)
print("\nSmoothing by Bin Mean:")
for b in bins:
    mean = sum(b) / len(b)
    print([round(mean, 2)] * len(b))
print("\nSmoothing by Bin Median:")
for b in bins:
    median = sorted(b)[len(b) // 2]
    print([median] * len(b))
print("\nSmoothing by Bin Boundaries:")
for b in bins:
    low = b[0]
    high = b[-1]
    boundary_bin = []
    for x in b:
        if abs(x - low) <= abs(x - high):
            boundary_bin.append(low)
        else:
            boundary_bin.append(high)
    print(boundary_bin)
