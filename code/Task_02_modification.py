import numpy as np

# New real-world case: 7 days of rainfall in millimeters
rainfall_mm = np.array([12.5, 0.0, 5.2, 18.1, 2.0, 0.0, 8.4])

total_rain = np.sum(rainfall_mm)
mean_rain = np.mean(rainfall_mm)
max_rain = np.max(rainfall_mm)

# Convert to inches (1 inch = 25.4 mm)
rainfall_inches = rainfall_mm / 25.4

print(f"Total weekly rainfall: {total_rain:.2f} mm")
print(f"Daily mean rainfall: {mean_rain:.2f} mm")
print(f"Maximum daily rainfall: {max_rain:.2f} mm")
print("Rainfall in inches:", np.round(rainfall_inches, 2))