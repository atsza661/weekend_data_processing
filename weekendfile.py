import pandas as pd
import datetime

# Read Saturday and Sunday data into separate dataframes
sat_df = pd.read_csv('data_2023-02-11.csv')
sun_df = pd.read_csv('data_2023-02-12.csv')

# Concatenate the dataframes vertically into one
combined_df = pd.concat([sat_df, sun_df], ignore_index=True)

# Add a new column for the combined file generation date
today = datetime.datetime.today().strftime('%Y-%m-%d')
combined_df['Combined file generation date'] = today

# Save the combined dataframe to a new CSV file
combined_df.to_csv('weekend_data.csv', index=False)
