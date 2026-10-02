grocery = ["Rice", "Milk", "Eggs", "Bread"]

# Add item
grocery.append("Sugar")

# Remove item
grocery.remove("Milk")

# Sort the list
grocery.sort()

print("Grocery List:")

for item in grocery:
    print(item)

print("Total items:", len(grocery))