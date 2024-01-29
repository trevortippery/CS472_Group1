import csv
import requests
import json

# GitHub repo
repo = 'scottyab/rootbeer'

# GitHub authentication token
token = "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"

# File with list of files
file_list = 'data/file_rootbeer.csv'

# Output file
output_file = 'data/file_authors_dates.csv'

def get_commit_history(file_path):
    url = f"https://api.github.com/repos/{repo}/commits?path={file_path}"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    return json.loads(response.text)

with open(file_list, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header

    with open(output_file, 'w') as out_file:
        csv_writer = csv.writer(out_file)
        csv_writer.writerow(["Filename", "Author", "Date"])  # Write header

        for row in csv_reader:
            file_path = row[0]
            commit_history = get_commit_history(file_path)

            for commit in commit_history:
                author = commit['commit']['author']['name']
                date = commit['commit']['author']['date']
                csv_writer.writerow([file_path, author, date])