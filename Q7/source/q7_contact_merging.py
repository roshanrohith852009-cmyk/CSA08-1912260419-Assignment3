
import time
import sys

contacts_a = {
    "Ravi": "9876543210",
    "Kumar": "9876501234",
    "Arun": "9876512345",
    "Mani": "9876523456"
}

contacts_b = {
    "Ravi": "9876543210",
    "Siva": "9876534567",
    "Kumar": "9999999999",
    "Bala": "9876545678"
}

print("CONTACT MERGING PROGRAM")

print("\nContact List A:")
print(contacts_a)

print("\nContact List B:")
print(contacts_b)

# Merge contacts
merged_contacts = contacts_a.copy()

for name, phone in contacts_b.items():
    if name not in merged_contacts:
        merged_contacts[name] = phone
    elif merged_contacts[name] != phone:
        print("\nConflict for", name)
        print("Number A:", merged_contacts[name])
        print("Number B:", phone)

        # Keep the original contact
        print("Keeping original number.")

print("\nMERGED CONTACT LIST")
for name, phone in merged_contacts.items():
    print(name, ":", phone)

# Identify common contacts
common_contacts = contacts_a.keys() & contacts_b.keys()

print("\nCommon Contact Names:")
print(common_contacts)

# Unique contacts
unique_contacts = (
    contacts_a.keys() ^ contacts_b.keys()
)

print("\nUnique Contact Names:")
print(unique_contacts)

# Add a new contact
merged_contacts["Raj"] = "9876556789"

# Search contact
search_name = input("\nEnter contact name to search: ").strip().title()

if search_name in merged_contacts:
    print("Phone Number:", merged_contacts[search_name])
else:
    print("Contact not found.")

print("\nTotal Contacts:", len(merged_contacts))

# Performance experiment
start = time.perf_counter()

for _ in range(100000):
    result = merged_contacts.get("Ravi")

end = time.perf_counter()

print("\nLookup Time:", end - start, "seconds")
print("Memory Used:", sys.getsizeof(merged_contacts), "bytes")
