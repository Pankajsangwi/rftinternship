def analyze_scores(marks):
    n = len(marks)
    
    # Initialize variables
    total = 0
    highest = lowest = marks[0]
    
    # Single loop for sum, min, max
    for m in marks:
        total += m
        if m > highest:
            highest = m
        if m < lowest:
            lowest = m
    
    # Average
    avg = total / n
    
    # Count above average
    above_avg = 0
    for m in marks:
        if m > avg:
            above_avg += 1
    
    # Grade distribution
    grades = {"A": 0, "B": 0, "C": 0, "FAIL": 0}
    
    for m in marks:
        if m >= 90:
            grades["A"] += 1
        elif m >= 75:
            grades["B"] += 1
        elif m >= 50:
            grades["C"] += 1
        else:
            grades["FAIL"] += 1
    
    # Output
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Above Average Count:", above_avg)
    print("Grade Distribution:", grades)


# Given Data
marks = [78, 85, 90, 67, 85, 92, 78]

analyze_scores(marks)