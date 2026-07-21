from statistics import mean, median, multimode
pencils = [9, 25, 23, 12, 11, 6, 7, 8, 9, 10]
mean_value = mean(pencils)
median_value = median(pencils)
mode_value = multimode(pencils)
print("Pencils in Boxes:", pencils)
print("Mean =", round(mean_value, 2))
print("Median =", median_value)
print("Mode =", mode_value)
