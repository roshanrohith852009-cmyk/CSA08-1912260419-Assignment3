
import random
import time
import sys

# Generate sensor readings
readings = [
    random.choice([random.uniform(10, 100), -1, None, 0])
    for _ in range(50)
]

print("ORIGINAL SENSOR READINGS")
print(readings)

# Remove missing and invalid readings
cleaned = [
    value for value in readings
    if value is not None and value > 0
]

print("\nCLEANED READINGS")
print(cleaned)

# Convert values to two decimal places
rounded = [round(value, 2) for value in cleaned]

print("\nROUNDED READINGS")
print(rounded)

# Identify high readings
high_readings = [value for value in rounded if value > 75]

print("\nHIGH READINGS (>75):")
print(high_readings)

# Identify low readings
low_readings = [value for value in rounded if value <= 25]

print("\nLOW READINGS (<=25):")
print(low_readings)

# Calculate statistics
if rounded:
    print("\nMinimum:", min(rounded))
    print("Maximum:", max(rounded))
    print("Average:", round(sum(rounded) / len(rounded), 2))
else:
    print("\nNo valid sensor readings.")

# Compare normal loop and list comprehension
start = time.perf_counter()
for _ in range(10000):
    result = [x for x in readings if x is not None and x > 0]
end = time.perf_counter()

print("\nList Comprehension Time:", end - start, "seconds")
print("Memory Used:", sys.getsizeof(readings), "bytes")
