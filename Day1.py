data = [10, None, 20, 10, "", 30, None, 40]

clean_set = set()
removed_count = 0

for item in data:
    if item is None or item == "":
        removed_count += 1
    elif item not in clean_set:
        clean_set.add(item)
    else:
        removed_count += 1

# Sort final list
clean_list = sorted(clean_set)

print("Clean List:", clean_list)
print("Removed Values Count:", removed_count)