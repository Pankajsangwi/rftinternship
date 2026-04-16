import csv
# Given dataset
data = [
    ["A", 2, 100],
    ["B", 1, 200],
    ["A", 3, 100],
    ["C", 5, 50]
]

product_sales = {}
total_revenue = 0

# Process data
for product, qty, price in data:
    total = qty * price   # New column
    
    # Add to total revenue
    total_revenue += total
    
    # Aggregate per product
    if product in product_sales:
        product_sales[product] += total
    else:
        product_sales[product] = total

# Find top-selling product
top_product = max(product_sales, key=product_sales.get)

# Sort by revenue (descending)
sorted_sales = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

# Output
print("Total Sales Per Product:", product_sales)
print("Total Revenue:", total_revenue)
print("Top Selling Product:", top_product)
print("Sorted Sales:", sorted_sales)