students = {
    "Rahim": 80,
    "Karim": 75,
    "Sakib": 90,
    "Hasan": 65,
    "Rafi": 85
}

scores = list(students.values())

average = sum(scores) / 5
highest = max(scores)
lowest = min(scores)

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)

for name, score in students.items():
    print(name, ":", score)