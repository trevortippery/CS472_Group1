# Trevor Tippery
# CS472 
# 01/26/2024

# libraries
import matplotlib.pyplot as plt
import csv
from datetime import datetime

# path for the csv file
csvFile = "data/file_rootbeer.csv"

# data dictionary to store all filenames
# with touches of each file
data = {}

# read through csv file and collect data
with open(csvFile, newline='') as csvfile:

    reader = csv.reader(csvfile)
    # skip first row since csv has {filename, touches} as header
    next(reader)  

    for row in reader:
        filename, touchesStr = row
        # safely evaluate the string as a list
        touches = eval(touchesStr)
        data[filename] = touches

# makes each author a unique color
authors = set(author for touches in data.values() for author, _ in touches)
authorColorMap = {author: plt.cm.tab10(i) for i, author in enumerate(authors)}

# changes filenames and makes them numbers on the x-axis
file2int = {filename: i for i, 
               filename in enumerate(data.keys())}

# make x,y, and colors list for scatter plot
x = []
y = []
colors = []

# made a reference date as the first date a commit was ever made to the repo
reference = datetime(2015, 6, 19)

# main loop for plotting
for filename, touches in data.items():

    # gets int representation of filename
    fileNumber = file2int[filename]  

    # extracting data for each touch
    for author, touchDate in touches:
        # convert to datetime format
        touch = datetime.fromisoformat(touchDate.split('T')[0])  
        # calculates number of weeks to be plotted on scatter plot accordingly
        weeks = (touch - reference).days // 7
        x.append(fileNumber)
        y.append(weeks)
        colors.append(authorColorMap[author])

csvfile.close()

# creates scatter plot
plt.scatter(x, y, c=colors)
plt.xlabel('Files')
plt.ylabel('Weeks')
plt.show()
