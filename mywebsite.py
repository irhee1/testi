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
latitude -= 200
df = pd.DataFrame({
    "lon":[longitude],
    "lat":[latitude]})
st.header("This is your location!")
st.map(df)
