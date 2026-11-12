
import time
import sys

student_a = {"AI", "Python", "Cloud Computing", "Cyber Security"}
student_b = {"Python", "Data Science", "Cloud Computing", "IoT"}
student_c = {"AI", "Data Science", "IoT", "Robotics"}

print("ELECTIVE REGISTRATION ANALYSIS")

# Common electives
common_ab = student_a & student_b
print("\nCommon electives A and B:", common_ab)

# All registered electives
all_electives = student_a | student_b | student_c
print("All Unique Electives:", all_electives)

# Electives registered by only one student
unique_a = student_a - student_b
print("Unique to Student A:", unique_a)

# Symmetric difference
different_ab = student_a ^ student_b
print("Different Electives A and B:", different_ab)

# Detect clashes
students = {
    "Student A": student_a,
    "Student B": student_b,
    "Student C": student_c
}

print("\nCLASH REPORT")

names = list(students.keys())

for i in range(len(names)):
    for j in range(i + 1, len(names)):
        common = students[names[i]] & students[names[j]]
        if common:
            print(names[i], "and", names[j], ":", common)
        else:
            print(names[i], "and", names[j], ": No Clash")

# Performance experiment
start = time.perf_counter()
for _ in range(100000):
    result = student_a & student_b
end = time.perf_counter()

print("\nSet Operation Time:", end - start, "seconds")
print("Set Memory:", sys.getsizeof(student_a), "bytes")
