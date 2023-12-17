import streamlit as st
import requests

#api key and NASA url
api_key = "api_key=EEAf1Fdl3yzfxULiCOvFo5N2WjFbdNsFaz2WiR0P"
url = f"https://api.nasa.gov/planetary/apod?{api_key}"

#makle requst data as a dictionar
request = requests.get(url)

#get a gdictionare with dataclasses
content = request.json()

print(content)
#extract image, title, url, and explanation
image_title = content['title']
image_url = content['url']
image_text = content['explanation']

response = requests.get(image_url)
image_file = "image.jpg"
with open(image_file, "wb") as file:
    file.write(response.content)

st.title(image_title)
st.image(image_file)
st.write(image_text)
