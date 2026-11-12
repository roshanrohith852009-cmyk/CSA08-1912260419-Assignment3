
import random
import time
import sys

# Generate 365 daily rainfall readings (mm)
readings = [random.randint(0, 100) for _ in range(365)]

print("DAILY RAINFALL ANALYSIS")
print("Total readings:", len(readings))

# Calculate weekly rainfall totals
weekly_totals = [
    sum(readings[i:i + 7])
    for i in range(0, 364, 7)
]

# Include the final day in the last week
weekly_totals[-1] += readings[364]

print("\nWeekly Rainfall Totals:")
for week, total in enumerate(weekly_totals, 1):
    print(f"Week {week}: {total} mm")

print("\nWettest Week:", weekly_totals.index(max(weekly_totals)) + 1)
print("Driest Week:", weekly_totals.index(min(weekly_totals)) + 1)

# Seven-day moving average
moving_averages = [
    sum(readings[i:i + 7]) / 7
    for i in range(len(readings) - 6)
]

print("\nFirst 10 Moving Averages:")
print([round(x, 2) for x in moving_averages[:10]])

# Identify dry days
dry_days = [i + 1 for i, value in enumerate(readings) if value == 0]

print("\nDry Days:", dry_days)
print("Total Dry Days:", len(dry_days))

# Demonstrate slicing
print("\nSLICING EXAMPLES")
print("readings[7:14]:", readings[7:14])
print("readings[-7:]:", readings[-7:])
print("readings[::7]:", readings[::7])

# Performance measurement
start = time.perf_counter()
for _ in range(1000):
    [sum(readings[i:i + 7]) for i in range(359)]
end = time.perf_counter()

print("\nExecution Time:", end - start, "seconds")
print("Memory Used:", sys.getsizeof(readings), "bytes")
