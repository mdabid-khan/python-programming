profile = {
    "name": "Abid",
    "age": 20,
    "favorite_color": "Blue"
}

# Update age
profile["age"] = 21

# Add new field
profile["hobby"] = "Gaming"

# Remove favorite color
profile.pop("favorite_color")

# Print all key-value pairs
for key, value in profile.items():
    print(key, ":", value)