import json  # Import the JSON module to work with JSON data

# Open the JSON file named "sent_json" in read mode
with open("sent_json", "r") as f:
    data = json.load(f)  # Load the JSON content into a Python dictionary

# Create a lookup dictionary for gender:
# Maps gender_id -> gender label (e.g., 1 -> "Male")
gender_lookup = {g["gender_id"]: g["label"] for g in data["gender"]}

# Create a lookup dictionary for cars:
# Maps car_id -> full car object (so we can easily access its properties later)
car_lookup = {c["car_id"]: c for c in data["cars"]}

# Create a lookup dictionary for colors:
# Maps color label -> full color object (e.g., "red" -> {label: "red", rgbCode: "#FF0000"})
color_lookup = {c["label"]: c for c in data["rgbCode"]}

# Create a lookup dictionary for countries:
# Maps user_id -> country label
country_lookup = {}

# Loop through each country entry
for country in data["countries"]:
    # Each country has a list of users
    for user in country["user_ids"]:
        # Map each user's ID to the country's label
        country_lookup[int(user["userId"])] = country["label"]

# This will store the final transformed results
results = []

# Loop through each student in the dataset
for student in data["students"]:

    # Look up the student's gender label using gender_id
    gender = gender_lookup[student["gender_id"]]

    # Look up the student's "adore_car" (favorite car) using its ID
    adore = car_lookup[student["adore_car"]]

    # Create a simplified dictionary for the adored car
    adore_car = {
        "car_brand": adore["car_brand"],   # Brand name (e.g., Toyota)
        "brand_from": adore["car_make"]    # Country or maker of the brand
    }

    # Convert list of car IDs into a list of car brand names
    car_brands = [car_lookup[c]["car_brand"] for c in student["car_brand"]]

    # Convert list of color labels into full color objects (including RGB codes)
    colors = [color_lookup[c] for c in student["color"]]

    # Get the country of the student using user_id
    # .get() is used to avoid errors if the user_id is not found
    country = country_lookup.get(student["user_id"])

    # Build the final structured result for this student
    result = {
        "user_id": student["user_id"],
        "first_name": student["first_name"],
        "last_name": student["last_name"],
        "gender": gender,
        "adore_car": adore_car,
        "car_brand": car_brands,
        "countries": country,
        "colors": colors
    }

    # Add the processed student data to the results list
    results.append(result)

# Print the final results as a nicely formatted JSON string
print(json.dumps(results, indent=2))