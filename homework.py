import requests
import streamlit as st

api_key = "7usiLj3Ddn4Q7dbIFhY12eDgI7qJa5eVMsdmFAn8"

url =("https://api.nasa.gov/planetary/apod?"
      f"api_key={api_key}")

# Make a request to the API
request = requests.get(url)

# Convert the response to JSON
data = request.json()

# Access the title and explanation
title = data["title"]
text = data["explanation"]

# Picture of the day
picture_url = data["hdurl"]
picture_response = requests.get(picture_url)
picture = picture_response.content

# Save the picture
with open("picture.jpg", "wb") as file:
    file.write(picture)

st.set_page_config(layout="wide")
st.title(title)
st.image("picture.jpg", use_column_width=True)
st.write(text)




