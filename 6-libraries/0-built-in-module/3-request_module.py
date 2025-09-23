import sys
import requests
'''
# Base URL for posts
url = "https://jsonplaceholder.typicode.com/posts"

# Optional: Take user input for number of posts to show
if len(sys.argv) > 1:
    try:
        limit = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid number")
        sys.exit(1)
else:
    limit = 5  # default number of posts

# Make GET request
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    sys.exit(1)

# Parse JSON
data = response.json()

# Print post titles
for post in data[:limit]:
    print(f"Post ID: {post['id']}, Title: {post['title']}")
'''
"https://itunes.apple.com/search?entity=song&limit=50&term="
import json

if len(sys.argv)!=2:
    sys.exit()

response=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])
# print(json.dumps(response.json()))

o=response.json()
for results in o["results"]:
    print(results["trackName"])









