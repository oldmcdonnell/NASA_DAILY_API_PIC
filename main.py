import streamlit as st
import pandas
import requests
st.set_page_config(layout="wide")

api_key = "api_key=EEAf1Fdl3yzfxULiCOvFo5N2WjFbdNsFaz2WiR0P"
url = f"https://api.nasa.gov/planetary/apod?{api_key}"

#makle requst
request = requests.get(url)

#get a gdictionare with dataclasses
content = request.json()

print(content)
image_file = content['hdurl']
image_text = content['explanation']
print(image_file)
print(image_text)
response = requests.get(image_file)
with open("image.jpg", "wb") as file:
    file.write(response.content)

