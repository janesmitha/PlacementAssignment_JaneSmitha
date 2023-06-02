'''Question 4 -
Write a program to download the data from the link given below and then read the data and convert the into
the proper structure and return it as a CSV file.
Link - https://data.nasa.gov/resource/y77d-th95.json
Note - Write code comments wherever needed for code understanding.

Sample Data -

Excepted Output Data Attributes
● Name of Earth Meteorite - string id - ID of Earth
● Meteorite - int nametype - string recclass - string
● mass - Mass of Earth Meteorite - float year - Year at which Earth
● Meteorite was hit - datetime format reclat - float recclong - float
● point coordinates - list of int'''
import requests
import csv

# Step 1: Download the data
url = "https://data.nasa.gov/resource/y77d-th95.json"
response = requests.get(url)
data = response.json()

# Step 2: Convert the data into the proper structure
structured_data = []
for meteorite in data:
    attributes = {
        "name": meteorite["name"],
        "id": meteorite["id"],
        "nametype": meteorite["nametype"],
        "recclass": meteorite["recclass"],
        "mass": float(meteorite["mass (g)"]) if "mass (g)" in meteorite else None,
        "year": meteorite["year"] if "year" in meteorite else None,
        "reclat": float(meteorite["reclat"]) if "reclat" in meteorite else None,
        "reclong": float(meteorite["reclong"]) if "reclong" in meteorite else None,
        "coordinates": [float(meteorite["reclong"]), float(meteorite["reclat"])] if "reclong" in meteorite and "reclat" in meteorite else None
    }
    structured_data.append(attributes)

# Step 3: Save the data as a CSV file
filename = "meteorite_data.csv"
with open(filename, "w", newline="",encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=structured_data[0].keys())
    writer.writeheader()
    writer.writerows(structured_data)

print(f"Data saved as {filename}")
