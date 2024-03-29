import streamlit as st
import pandas as pd
import json
from urllib.request import urlopen
url='http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
a = data["loc"]
num = 0
while True:
    b = a[num:num + 1]
    if b == ",":
        longitude = a[num + 1:]
        latitude = a[:num - 1]
        break
    num += 1
latitude = float(latitude)
longitude = float(longitude)
latitude -= 8.2111
longitude -= 0.90145
df = pd.DataFrame({
    "lon":[longitude],
    "lat":[latitude]})
st.set_page_config(page_title="Find your location", layout="wide", page_icon="🗺️")
st.header("This is your location!")
st.map(df)

