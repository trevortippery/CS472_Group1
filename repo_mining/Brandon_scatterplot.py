import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Read the CSV file
df = pd.read_csv('data/file_authors_dates.csv')

# Convert 'Date' to datetime and extract the week
df['Date'] = pd.to_datetime(df['Date'])
df['Week'] = df['Date'].dt.isocalendar().week

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
                alpha=0.5)

plt.ylabel('Weeks')
plt.xlabel('Number of Files')
plt.title('Author Activities Over Time')

plt.savefig('data/scatter_plot.png')