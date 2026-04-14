data_list = []
total_marks = 0
count = 0

with open("data.csv", "r") as file:
    headers = file.readline().strip().split(",")

    for line in file:
        values = line.strip().split(",")

        # Handle missing values
        values = [v if v != "" else "0" for v in values]

        # Create dictionary
        record = dict(zip(headers, values))

        # Convert to integers
        record["AGE"] = int(record["AGE"])
        record["MARKS"] = int(record["MARKS"])

        # Add to list
        data_list.append(record)

        # For average calculation
        total_marks += record["MARKS"]
        count += 1

# Calculate average
average = total_marks / count if count > 0 else 0

# Output
print("Data:", data_list)
print("Average Marks:", average)