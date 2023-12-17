import streamlit as st
import pandas
import requests
st.set_page_config(layout="wide")
col1 = st.columns(1)

api_key = "api_key=EEAf1Fdl3yzfxULiCOvFo5N2WjFbdNsFaz2WiR0P"
url = f"https://api.nasa.gov/planetary/apod?{api_key}"

#makle requst
request = requests.get(url)

#get a gdictionare with dataclasses
content = request.json()

print(content)
image_title = content['title']
image_url = content['hdurl']
image_text = content['explanation']

response = requests.get(image_url)
image_file = "image.jpg"
with open(image_file , "wb") as file:
    file.write(response.content)

st.title(image_title)
st.image(image_file)
st.write(image_text)
