
import time
import sys

timetable = {
    "Chennai": {
        "train_101": {"destination": "Bangalore", "departure": "06:00", "arrival": "11:00"},
        "train_102": {"destination": "Coimbatore", "departure": "08:30", "arrival": "15:00"}
    },
    "Madurai": {
        "train_201": {"destination": "Chennai", "departure": "07:00", "arrival": "14:00"},
        "train_202": {"destination": "Trichy", "departure": "09:00", "arrival": "11:30"}
    },
    "Coimbatore": {
        "train_301": {"destination": "Salem", "departure": "10:00", "arrival": "13:00"}
    }
}

print("RAILWAY TIMETABLE")

# Display complete timetable
for station, trains in timetable.items():
    print("\nStation:", station)

    for train_id, details in trains.items():
        print(
            train_id,
            "| Destination:", details["destination"],
            "| Departure:", details["departure"],
            "| Arrival:", details["arrival"]
        )

# Search for a station
search_station = input("\nEnter station name to search: ").strip().title()

if search_station in timetable:
    print("\nTrains at", search_station)
    for train_id, details in timetable[search_station].items():
        print(train_id, details)
else:
    print("Station not found.")

# Search for destination
destination = input("\nEnter destination to search: ").strip().title()

print("\nMatching Trains:")

found = False

for station, trains in timetable.items():
    for train_id, details in trains.items():
        if details["destination"].lower() == destination.lower():
            print(station, train_id, details)
            found = True

if not found:
    print("No trains found.")

# Add a new train
timetable["Chennai"]["train_103"] = {
    "destination": "Hyderabad",
    "departure": "17:00",
    "arrival": "05:00"
}

print("\nUpdated Train Count:",
      sum(len(trains) for trains in timetable.values()))

# Timing and memory
start = time.perf_counter()
for _ in range(10000):
    result = timetable.get("Chennai")
end = time.perf_counter()

print("\nLookup Time:", end - start, "seconds")
print("Memory Used:", sys.getsizeof(timetable), "bytes")
