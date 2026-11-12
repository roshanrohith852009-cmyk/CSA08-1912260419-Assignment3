
import time
import sys

complaints = {
    101: {"farmer": "Ravi", "category": "Water", "status": "Pending"},
    102: {"farmer": "Kumar", "category": "Electricity", "status": "Resolved"},
    103: {"farmer": "Arun", "category": "Water", "status": "Pending"},
    104: {"farmer": "Mani", "category": "Crop Damage", "status": "Pending"},
    105: {"farmer": "Siva", "category": "Electricity", "status": "Resolved"},
    106: {"farmer": "Raj", "category": "Water", "status": "Resolved"}
}

print("FARMER COMPLAINT ANALYSIS")

# Display all complaints
for complaint_id, details in complaints.items():
    print(complaint_id, details)

# Count complaint categories
category_count = {}

for details in complaints.values():
    category = details["category"]
    category_count[category] = category_count.get(category, 0) + 1

print("\nCategory Counts:")
print(category_count)

# Count complaint status
status_count = {}

for details in complaints.values():
    status = details["status"]
    status_count[status] = status_count.get(status, 0) + 1

print("\nStatus Counts:")
print(status_count)

# Identify pending complaints
pending = {
    cid: details
    for cid, details in complaints.items()
    if details["status"] == "Pending"
}

print("\nPending Complaints:")
print(pending)

# Update complaint
complaints[101]["status"] = "Resolved"

print("\nUpdated Complaint 101:")
print(complaints[101])

# Add new complaint
complaints[107] = {
    "farmer": "Bala",
    "category": "Water",
    "status": "Pending"
}

print("\nTotal Complaints:", len(complaints))

# Timing experiment
start = time.perf_counter()
for _ in range(100000):
    result = complaints.get(101)
end = time.perf_counter()

print("\nDictionary Lookup Time:", end - start, "seconds")
print("Memory Used:", sys.getsizeof(complaints), "bytes")
