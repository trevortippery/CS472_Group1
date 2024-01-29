import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('data/file_authors_dates.csv')

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Calculate the number of weeks from the minimum date
df['Week'] = (df['Date'] - df['Date'].min()).dt.days // 7

# Count the number of files modified by each author per week
df = df.groupby(['Author', 'Week']).size().reset_index(name='Files')

# Create a color dictionary for each unique author
colors = {author: np.random.rand(3,) for author in df['Author'].unique()}

# Create a scatter plot
plt.figure(figsize=(10, 6))
for author in df['Author'].unique():
    plt.scatter(df[df['Author'] == author]['Files'], 
                df[df['Author'] == author]['Week'], 
                c=[colors[author]], 
                alpha=0.5, 
                label=author)  # Add a label for the legend

plt.ylabel('Weeks')
plt.xlabel('Number of Files')
plt.title('Author Activities Over Time')

# Set the range of each axis
plt.xlim(0, df['Files'].max() + 10)  # Adjust as needed
plt.ylim(0, df['Week'].max() + 10)  # Adjust as needed

# Display the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.savefig('data/scatter_plot.png', bbox_inches='tight')

# Calculate total number of files modified by each author
total_files_by_author = df.groupby('Author')['Files'].sum()