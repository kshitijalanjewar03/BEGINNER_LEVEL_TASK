# List of friends' names
friends = ["Aditya", "Sneha", "Rahul", "Anjali", "Kiran"]

# Create list of tuples (name, length of name)
friends_with_length = [(name, len(name)) for name in friends]

# Print the result
print(friends_with_length)
