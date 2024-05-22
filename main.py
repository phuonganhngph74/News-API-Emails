import requests

api_key = "7462b0b10eca4e14aebb7ec31c35b191"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-04-22&sortBy"
       "=publishedAt&apiKey=7462b0b10eca4e14aebb7ec31c35b191")

# Make a request to the API
request = requests.get(url)

# Convert the response to JSON
content = request.json()

# Access the articles titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])


