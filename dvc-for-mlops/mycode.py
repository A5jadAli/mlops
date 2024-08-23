import pandas as pd
import os

# create a sample dataframe with names, ages and cities
data = {
    'Name': ['Tom', 'Nick', 'John', 'Smith', 'Sam'],
    'Age': [20, 21, 19, 18, 22],
    'City': ['New York', 'California', 'Texas', 'Florida', 'Washington']
}

df = pd.DataFrame(data)

# adding new row in data for V2
new_row = {'Name': 'Alex', 'Age': 25, 'City': 'New Jersey'}
df.loc[len(df.index)] = new_row

data_dir = 'data' # directory to save the data
os.makedirs(data_dir, exist_ok=True) # create the directory if it doesn't exist

# define the file path to save the data
file_path = os.path.join(data_dir, 'sample_data.csv')  # data/sample_data.csv

# save the dataframe to a csv file
df.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")