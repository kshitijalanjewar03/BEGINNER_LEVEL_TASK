# Define the cities for each country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Function to find the country of a city
def find_country(city):
    if city in Australia:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in India:
        return "India"
    else:
        return None

# Ask user to enter two cities
city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()

# Find the countries of both cities
country1 = find_country(city1)
country2 = find_country(city2)

# Check and print the result
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list.")
