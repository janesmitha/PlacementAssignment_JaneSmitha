'''Using the data from Question 4, write code to analyze the data and answer the following questions Note -
1. Draw plots to demonstrate the analysis for the following questions for better visualizations
2. Write code comments wherever required for code understanding

Insights to be drawn -
● Get all the Earth meteorites that fell before the year 2000
● Get all the earth meteorites co-ordinates who fell before the year 1970
● Assuming that the mass of the earth meteorites was in kg, get all those whose mass was more
than 10000kg'''

import requests
import matplotlib.pyplot as plt

# Step 1: Read and load the JSON data
url = "https://data.nasa.gov/resource/y77d-th95.json"
response = requests.get(url)
data = response.json()

# Lists to store the results for each question
earth_meteorites_before_2000 = []
coordinates_before_1970 = []
mass_more_than_10000kg = []

# Step 2: Analysis and answering the questions
for meteorite in data:
    if "year" in meteorite:
        year = meteorite["year"]
        if year and int(year[:4]) < 2000:
            # Question 1: Get all the Earth meteorites that fell before the year 2000
            earth_meteorites_before_2000.append(meteorite)

            if int(year[:4]) < 1970:
                # Question 2: Get all the Earth meteorites' coordinates that fell before the year 1970
                if "reclat" in meteorite:
                    latitude = float(meteorite["reclat"])
                elif "reclat (degrees)" in meteorite:
                    latitude = float(meteorite["reclat (degrees)"])
                else:
                    continue

                if "reclong" in meteorite:
                    longitude = float(meteorite["reclong"])
                elif "reclong (degrees)" in meteorite:
                    longitude = float(meteorite["reclong (degrees)"])
                else:
                    continue

                coordinates = (latitude, longitude)
                coordinates_before_1970.append(coordinates)

    mass = None
    if "mass (g)" in meteorite:
        mass = meteorite["mass (g)"]
    elif "mass (kg)" in meteorite:
        mass = float(meteorite["mass (kg)"]) * 1000  # Convert kg to g

    if mass and mass > 10000:
        # Question 3: Get all the Earth meteorites whose mass was more than 10000kg (assuming mass is in grams)
        mass_more_than_10000kg.append(meteorite)

# Step 3: Visualization
# Plotting the number of Earth meteorites fell before the year 2000 and before the year 1970
labels = ["Before 2000", "Before 1970"]
values = [len(earth_meteorites_before_2000), len(coordinates_before_1970)]

plt.bar(labels, values)
plt.xlabel("Year")
plt.ylabel("Number of Meteorites")
plt.title("Analysis of Earth Meteorites")
plt.show()

# Printing the results
print("Earth meteorites that fell before the year 2000:")
for meteorite in earth_meteorites_before_2000:
    print(meteorite.get("name", ""))

print("\nEarth meteorites coordinates that fell before the year 1970:")
for coordinates in coordinates_before_1970:
    print(coordinates)

print("\nEarth meteorites with mass more than 10000kg:")
for meteorite in mass_more_than_10000kg:
    print(meteorite.get("name", ""))
