from statistics import mean, median, multimode
ages = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22,
        25, 25, 25, 25, 30, 33, 33, 35, 35, 35,
        35, 36, 40, 45, 46, 52, 70]
mean_value = mean(ages)
median_value = median(ages)
mode_value = multimode(ages)
midrange = (min(ages) + max(ages)) / 2
n = len(ages)
lower_half = ages[:n//2]
upper_half = ages[n//2 + 1:]
Q1 = median(lower_half)
Q3 = median(upper_half)
print("Mean =", round(mean_value, 2))
print("Median =", median_value)
print("Mode =", mode_value)
if len(mode_value) == 1:
    print("Modality = Unimodal")
elif len(mode_value) == 2:
    print("Modality = Bimodal")
elif len(mode_value) == 3:
    print("Modality = Trimodal")
else:
    print("Modality = Multimodal")
print("Midrange =", midrange)
print("First Quartile (Q1) =", Q1)
print("Third Quartile (Q3) =", Q3)
