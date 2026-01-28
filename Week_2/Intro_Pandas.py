# Pandas is a python library used for data manipulation and analysis
# it provides data stuctures like DataFrames and Series to work with structured data
# it also offers functionalities for data cleaning, transformation, aggregation, and visualization

import pandas as pd
import matplotlib.pyplot as plt

# # Create a simple DataFrame
# data = {
#     'Name' : ['Alice', 'David', 'Charlie', 'Bob'],
#     'Age' : [24, 42, 19, 88],
#     'City' : ['New York', 'Los Angeles', 'Chicago', 'Houston']
# }

# df = pd.DataFrame(data)

# print(f"{df}")

# # Access rows by index location
# print(f"\nFirst Row:\n{df.iloc[2]}")

# # Acces colums
# print(f"\nNames Column:\n{df['Name']}")

# # filter data using a condition
# olderThan30 = df[df['Age'] >= 30]

# print(f"\nAdults 30+:\n{olderThan30}")

# # Add a new column
# df['Occupation'] = ['Nurse', 'Biologist', 'Chef', 'Engineer']

# print(f"\nNew Occupation Column:\n{df}")

# # Simple stats calculations
# print(f"\nAverage Age:\n{df['Age'].mean()}")
# print(f"\nMaximum Age:\n{df['Age'].max()}")
# print(f"\nSummary Statistics\n{df.describe()}")

# # Sort the data
# sorted_df = df.sort_values(by = 'Age')
# print(f"\nSorted by Age:\n{sorted_df}")



# ===== Accessing data from CSV =====
vehicle_df = pd.read_csv("./data/Electric_Vehicle_Population_data.csv")

# print(f"\nVehicle DataFrame:\n{vehicle_df.head()}")
# print(f"\nVehicle DataFrame:\n{vehicle_df.info()}")

# Basic selection and filtering
# select each unique vehicle make
vehicle_makes = vehicle_df['Make'].unique()

# print(f"\nUnique Makes:\n{vehicle_makes}")

# filter vehicles made by Tesla
# tesla_vehicle = vehicle_df[vehicle_df['Make'] == 'TESLA']

# print(f"\nTesla Vehicles:\n{tesla_vehicle.head(10)}")

# Filter using NOT using the ~ operator in pandas
non_tesla_vehicles = vehicle_df[~(vehicle_df['Make'] == 'TESLA')]

# print(f"\nNot Teslas:\n{non_tesla_vehicles.head(10)}")

# We can aggregate some data
# get average electric range by vehicle make
# and filter out 0 values
avg_range_by_make = vehicle_df[vehicle_df['Electric Range'] > 0].groupby('Make')['Electric Range'].mean()

# print(f"\nAverage Range of Electric Car by Make:\n{avg_range_by_make}")

# double_aggro = vehicle_df.groupby('Make').agg(
#     avg_range = ('Electric Range', 'mean'),
#     sum_legis_dis = ('Legislative District', 'sum')
# )

# print(double_aggro)

# Finally, we can visualize our data using matplotlib
# We can create a Figure - a matplotlib object that represents the entire figure/plot area
fig, axes = plt.subplots(2, 2, figsize = (12, 12))

# Plot the average electric range by vehicle as a bar chart
avg_range_by_make.plot(kind = 'bar', ax = axes[0, 0], title = "Average Electric Range by Vehicle Make", xlabel = 'Vehicle Make', ylabel = 'Average Electric Range (miles)')


# plot the count of non tesla vehicles by model year
non_tesla_vehicles['Model Year'].value_counts().sort_index().plot(kind = 'bar', ax = axes[0,1], 
    title = 'Count of Non-Tesla by Model Year', xlabel = 'Mode Year', ylabel = 'Number of Vehicles')

plt.show()

# FINALLY, we can export our modified DataFrame to a new CSV file
non_tesla_vehicles.to_csv("./data/modified_vehicle_data.csv", index = False)