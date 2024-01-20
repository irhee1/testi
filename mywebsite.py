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
latitude -= 0.0032
longitude += 0.0036
df = pd.DataFrame({
    "lon":[longitude],
    "lat":[latitude]})
st.header("This is your location!")
st.map(df)
st.subheader("The city you are currently in is named "+ data['city'])
if data['country'] == "US":
    st.subheader("The state you are currently in is named " + data['region'])
else:
    st.subheader("The region you are currently in is named " + data['region'])
st.subheader("The country you are currently in is named " + data['country'])
