lower = [1, 5, 15, 20, 50, 80]
upper = [5, 15, 20, 50, 80, 110]
freq = [200, 450, 300, 1500, 700, 44]
N = sum(freq)
cf = []
total = 0
for f in freq:
    total += f
    cf.append(total)
median_pos = N / 2
for i in range(len(cf)):
    if cf[i] >= median_pos:
        median_class = i
        break
L = lower[median_class]
f = freq[median_class]

if median_class == 0:
    cf_prev = 0
else:
    cf_prev = cf[median_class - 1]
h = upper[median_class] - lower[median_class]
median = L + ((median_pos - cf_prev) / f) * h
print("Total Frequency =", N)
print("Median Position =", median_pos)
print("Median Class =", f"{lower[median_class]}-{upper[median_class]}")
print("Approximate Median =", round(median, 2))
