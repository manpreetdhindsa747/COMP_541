import pandas as pd

# Sample data
data = {'ID': [1, 2, 3, 4, 5],
        'Category': [1, 2, 1, 3, 2]}

df = pd.DataFrame(data)

# Define a mapping of integer values to category names
category_mapping = {
    1: 'Category A',
    2: 'Category B',
    3: 'Category C'
}

# Map the integers in 'Category' column to category names
df['Category'] = df['Category'].map(category_mapping)

# Convert the 'Category' column to categorical
df['Category'] = df['Category'].astype('category')

# Check the data type of the 'Category' column
print(df.dtypes)