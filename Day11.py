import matplotlib.pyplot as plt

# Dataset
dates = ["MON", "TUE", "WED", "THU", "FRI"]
sales = [200, 250, 300, 280, 350]

# Find highest and lowest
max_sale = max(sales)
min_sale = min(sales)

max_day = dates[sales.index(max_sale)]
min_day = dates[sales.index(min_sale)]

# Plot line chart
plt.figure()
plt.plot(dates, sales, marker='o')

# Highlight highest point
plt.scatter(max_day, max_sale)
plt.text(max_day, max_sale, f' Highest: {max_sale}', ha='center')

# Highlight lowest point
plt.scatter(min_day, min_sale)
plt.text(min_day, min_sale, f' Lowest: {min_sale}', ha='center')

# Labels and title
plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Weekly Sales Trend")

# Grid (optional but good for analysis)
plt.grid()

# Show plot
plt.show()