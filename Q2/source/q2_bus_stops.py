
import time
import sys
import copy

# Immutable bus-stop information
bus_stops = (
    ("Stop A", 10.5, 20.3),
    ("Stop B", 11.2, 21.4),
    ("Stop C", 12.5, 22.1),
    ("Stop D", 13.7, 23.6),
    ("Stop E", 14.8, 24.9)
)

print("BUS STOP MAP")
for stop in bus_stops:
    print(stop)

# Access tuple elements
print("\nFirst Stop:", bus_stops[0])
print("Last Stop:", bus_stops[-1])
print("Middle Stops:", bus_stops[1:4])

# Tuple immutability
try:
    bus_stops[0] = ("New Stop", 0, 0)
except TypeError as error:
    print("\nImmutability:", error)

# Copying
shallow_copy = copy.copy(bus_stops)
deep_copy = copy.deepcopy(bus_stops)

print("\nOriginal:", bus_stops)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)

print("\nOriginal and Shallow Copy Same Object:",
      bus_stops is shallow_copy)

# Convert to list for modification
modifiable_stops = list(bus_stops)
modifiable_stops.append(("Stop F", 15.5, 25.8))

print("\nModified List:")
print(modifiable_stops)

# Timing experiment
start = time.perf_counter()
for _ in range(100000):
    value = bus_stops[2]
end = time.perf_counter()

print("\nAccess Time:", end - start, "seconds")
print("Tuple Memory:", sys.getsizeof(bus_stops), "bytes")
