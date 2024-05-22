import requests
from send_email import send_email

topic = "tesla"

api_key = "7462b0b10eca4e14aebb7ec31c35b191"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2024-04-22&"
       "sortBy=publishedAt&"
       "apiKey=7462b0b10eca4e14aebb7ec31c35b191&"
       "language=en")

# Make a request to the API
request = requests.get(url)

# Convert the response to JSON
content = request.json()

message = "Subject: Today's news about Tesla\n\n"

# Access the articles titles and descriptions
for article in content["articles"][:20]:

    if article["title"] is not None:
        message += f"Title {article['title']}\n"
        message += f"Description: {article['description']}\n"
        message += f"Read more: {article['url']}\n\n"

message = message.encode("utf-8")
# Call the send_email function
send_email(message=message)




