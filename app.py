import pandas as pd
import streamlit as st
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.crime
collection = db.crime_document

years = list(range(1980, 1985))

selected_date = st.selectbox("Year", years)

pipeline = [
    {"$match": {"Year": selected_date}},
    {"$group": {"_id": "$Weapon", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]

result = collection.aggregate(pipeline)

data = pd.DataFrame(result).set_index("_id")

st.bar_chart(data)