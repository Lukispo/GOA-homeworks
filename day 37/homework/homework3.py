temperatures = [72, 68, 75, 70, 78, 74, 71]

highest_temp = max(temperatures)
print("Highest Temperature:", highest_temp)

lowest_temp = min(temperatures)
print("Lowest Temperature:", lowest_temp)

average_temp = sum(temperatures) / len(temperatures)
print("Average Temperature:", average_temp)

above_70 = [temp for temp in temperatures if temp > 70]
print("Temperatures Above 70:", above_70)
