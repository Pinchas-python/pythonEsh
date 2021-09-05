import json

issue_data= open('issueData.json')
json_data = json.load(issue_data)

print(json_data)