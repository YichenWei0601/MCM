"""
Each country, each event. 
The number of medals each year.

-> weighed score and the score change.
"""


import pandas as pd

# Load the medal counts data
medal_counts_data = pd.read_csv(r"C:\Users\weiyi\Desktop\summerOly_athletes_sorted3.csv", encoding='latin1')

# Filter the necessary columns
dataset = medal_counts_data[['Name', 'NOC', 'Year', 'Sport', 'Medal']]

# Create a new column for medal count (Gold = 1, Silver = 2, Bronze = 3)
medal_map = {'Gold': 1, 'Silver': 2, 'Bronze': 3}
dataset['Medal_Num'] = dataset['Medal'].map(medal_map)

# Initialize a list to store the result
final_result = []

# Group data by NOC, Event, and Year, then calculate the required statistics
grouped = dataset.groupby(['NOC', 'Sport', 'Year']).agg(
    Gold=('Medal', lambda x: (x == 'Gold').sum()),
    Silver=('Medal', lambda x: (x == 'Silver').sum()),
    Bronze=('Medal', lambda x: (x == 'Bronze').sum()),
    No_Medal=('Medal', lambda x: (x.isnull()).sum()),
    Participants=('Name', 'nunique')
).reset_index()

# Calculate medal per participant
grouped['Gold_per_Participant'] = grouped['Gold'] / grouped['Participants']
grouped['Silver_per_Participant'] = grouped['Silver'] / grouped['Participants']
grouped['Bronze_per_Participant'] = grouped['Bronze'] / grouped['Participants']
grouped['No_Medal_per_Participant'] = grouped['No_Medal'] / grouped['Participants']

# Set the weights for each medal type (Gold = 8, Silver = 4, Bronze = 2, No Medal = 1)
W_gold = 4
W_silver = 2
W_bronze = 1
W_no_medal = 0

# Calculate the weighted sum of per-participant ratios
grouped['Weighted_Sum'] = (
    (grouped['Gold_per_Participant'] * W_gold) +
    (grouped['Silver_per_Participant'] * W_silver) +
    (grouped['Bronze_per_Participant'] * W_bronze) +
    (grouped['No_Medal_per_Participant'] * W_no_medal)
)

# Sort by NOC, Event, and Year for easy comparison
grouped.sort_values(by=['NOC', 'Sport', 'Year'], inplace=True)

# Merge with a shifted version of the dataframe to get the Weighted_Sum difference
grouped['Weighted_Sum_Diff'] = grouped.merge(
    grouped[['NOC', 'Sport', 'Year', 'Weighted_Sum']].assign(Year=grouped['Year'] + 4),
    on=['NOC', 'Sport', 'Year'],
    how='left',
    suffixes=('', '_Diff')
)['Weighted_Sum_Diff'] - grouped['Weighted_Sum']

# Calculate the absolute value of the Weighted_Sum_Diff
grouped['Weighted_Sum_Diff_Abs'] = grouped['Weighted_Sum_Diff'].abs()

# Define the bins for the ranges, with 0 as a separate category
bins = [0, 1, 2, 3, 4, 5, 6, float('inf')]  # define bins as [0, 1), [1, 2), ..., [5, 6), >6
labels = ['0', '0~1', '1~2', '2~3', '3~4', '4~5', '5~6']

# Use pd.cut() to categorize the absolute values into the defined ranges
grouped['Weighted_Sum_Diff_Category'] = pd.cut(grouped['Weighted_Sum_Diff_Abs'], bins=bins, labels=labels, right=False)

# Count the number of occurrences in each category
category_counts = grouped['Weighted_Sum_Diff_Category'].value_counts().sort_index()

# Print the result
print(category_counts)