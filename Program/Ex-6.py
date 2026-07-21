age = [23, 23, 27, 27, 39, 41, 47, 49, 50,
       52, 54, 54, 56, 57, 58, 58, 60, 61]
value = 35
min_age = min(age)
max_age = max(age)
min_max = (value - min_age) / (max_age - min_age)
mean_age = sum(age) / len(age)
std_dev = 12.94
z_score = (value - mean_age) / std_dev
max_value = max(age)
j = len(str(max_value))
decimal_scaling = value / (10 ** j)
print("Age Value =", value)
print("\n(i) Min-Max Normalization =", round(min_max, 4))
print("(ii) Z-Score Normalization =", round(z_score, 4))
print("(iii) Decimal Scaling Normalization =", round(decimal_scaling, 4))
