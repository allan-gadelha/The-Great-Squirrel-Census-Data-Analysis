import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231116.csv")

#First look at all the columns from the csv to see better on what i'm working on
for column_names in data:
    print(column_names)

#I figured out that the row i want is the Primary Fur Color
column_name = "Primary Fur Color"
selected_column = data[column_name]

#Converting my column to a list
column_list = selected_column.tolist()
#print(column_list)

# Count the occurrences of 'Gray', 'Cinnamon', and 'Black'
gray_count = column_list.count('Gray')
cinnamon_count = column_list.count('Cinnamon')
black_count = column_list.count('Black')

print(f"Gray: {gray_count}, Cinnamon: {cinnamon_count}, Black: {black_count}")

#After looking more, i've found a easier way to discover what i really wanted!
# Get counts of unique values in 'Primary Fur Color' column
color_counts = data['Primary Fur Color'].value_counts()

print(color_counts)
print(f"Gray: {color_counts['Gray']}, Cinnamon: {color_counts['Cinnamon']}, Black: {color_counts['Black']}")