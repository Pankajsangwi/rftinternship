logs = [
    "ERROR DISK FULL",
    "INFO STARTED",
    "ERROR FILE MISSING",
    "WARNING MEMORY LOW"
]

# Initialize counters
counts = {
    "ERROR": 0,
    "INFO": 0,
    "WARNING": 0
}

# Process logs (case insensitive)
for log in logs:
    log = log.upper()   # ignore case
    
    for key in counts:
        if key in log:
            counts[key] += 1

# Print counts
print("Log Counts:")
for key, value in counts.items():
    print(f"{key}: {value}")

# Find most frequent log type
most_frequent = max(counts, key=counts.get)
print("\nMost Frequent Log Type:", most_frequent)