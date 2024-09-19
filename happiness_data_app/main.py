import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("happiness_data_app/happy.csv")

st.title("In Search for Happiness")
options = ("Happiness", "GDP", "Generosity")
option1 = st.selectbox("Select the data for the X-axis", options)
option2 = st.selectbox("Select the data for the Y-axis", options)
st.subheader(f"{option1} and {option2}")

x_data = df[option1.lower()]
y_data = df[option2.lower()]

figure = px.scatter(x=x_data, y=y_data, labels={"x": option1, "y": option2})
st.plotly_chart(figure)