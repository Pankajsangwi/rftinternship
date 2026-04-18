# Sample dataset (you can modify or load from file)
data = [
    {"name": "Amit", "salary": 60000, "age": 25},
    {"name": "Riya", "salary": 45000, "age": 28},
    {"name": "John", "salary": 70000, "age": 32},
    {"name": "Neha", "salary": 52000, "age": 27},
    {"name": "Raj", "salary": 48000, "age": 22}
]

# Filtering conditions
filtered_data = list(filter(
    lambda x: x["salary"] > 50000 and x["age"] < 30,
    data
))

# Display results
print("Filtered Results:")
for person in filtered_data:
    print(person)

# BONUS: Save to new file
import json

with open("filtered_data.json", "w") as file:
    json.dump(filtered_data, file, indent=4)

print("\nFiltered data saved to 'filtered_data.json'")