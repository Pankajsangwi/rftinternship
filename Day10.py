logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

# Dictionary to store counts
count = {}

# Process each log
for log in logs:
    log_type = log.split()[0].upper()   # take first word and ignore case

    if log_type in count:
        count[log_type] += 1
    else:
        count[log_type] = 1

# Print counts
print("Log Counts:")
for key, value in count.items():
    print(f"{key}: {value}")

# Find most frequent log type
max_count = max(count.values())
most_frequent = []

for key, value in count.items():
    if value == max_count:
        most_frequent.append(key)

print("\nMost Frequent Log Type:", ", ".join(most_frequent))