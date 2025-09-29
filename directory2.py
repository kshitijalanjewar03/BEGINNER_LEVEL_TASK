# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses
total_your = sum(your_expenses.values())
total_partner = sum(partner_expenses.values())

print(f"Your total expenses: {total_your}")
print(f"Partner's total expenses: {total_partner}")

# Determine who spent more
if total_your > total_partner:
    print("You spent more money overall.")
elif total_partner > total_your:
    print("Your partner spent more money overall.")
else:
    print("Both spent the same amount.")

# Find category with significant spending difference
max_diff = 0
category_with_max_diff = ""

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses.get(category, 0))
    if diff > max_diff:
        max_diff = diff
        category_with_max_diff = category

print(f"The category with the biggest spending difference is '{category_with_max_diff}' with a difference of {max_diff}.")
