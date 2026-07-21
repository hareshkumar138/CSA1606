import math
data = [200, 300, 400, 600, 1000]
min_val = min(data)
max_val = max(data)
print("Min-Max Normalization (0 to 1):")
for x in data:
    normalized = (x - min_val) / (max_val - min_val)
    print(f"{x} -> {normalized:.3f}")
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = math.sqrt(variance)
print("\nZ-Score Normalization:")
for x in data:
    z_score = (x - mean) / std_dev
    print(f"{x} -> {z_score:.3f}")
