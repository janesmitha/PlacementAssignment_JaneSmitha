'''Write a program to read the data from the following link, perform data analysis and answer the following
questions
Note -
1. Write code comments wherever required for code understanding
Link - https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD
Insights to be drawn -
● Get all the cars and their types that do not qualify for clean alternative fuel vehicle
● Get all TESLA cars with the model year, and model type made in Bothell City.
● Get all the cars that have an electric range of more than 100, and were made after
2015
● Draw plots to show the distribution between city and electric vehicle type'''
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the data from the CSV file
url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"
data = pd.read_csv(url)
# Print column names
print(data.columns)

# Step 2: Analysis and answering the questions
'''
# Question 1: Get all the cars and their types that do not qualify for clean alternative fuel vehicle
non_clean_fuel_cars = data[data['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] == 'No'][['Make', 'Model Type']]
print("Cars that do not qualify for clean alternative fuel vehicle:")
print(non_clean_fuel_cars)

# Question 2: Get all TESLA cars with the model year, and model type made in Bothell City
tesla_cars_bothell = data[(data['Make'] == 'TESLA') & (data['City'] == 'BOTHELL')][['Model Year', 'Model Type']]
print("\nTESLA cars made in Bothell City:")
print(tesla_cars_bothell)

# Question 3: Get all the cars that have an electric range of more than 100, and were made after 2015
electric_cars_range_gt_100 = data[(data['Electric Range'] > 100) & (data['Model Year'] > 2015)][['Make', 'Model Type']]
print("\nCars with electric range > 100 and made after 2015:")
print(electric_cars_range_gt_100)

# Step 3: Visualization
# Plotting the distribution between city and electric vehicle type
city_ev_type_count = data.groupby(['City', 'Electric Vehicle Type']).size().unstack()
city_ev_type_count.plot(kind='bar', stacked=True)
plt.xlabel('City')
plt.ylabel('Count')
plt.title('Distribution of City and Electric Vehicle Type')
plt.show()'''

