import streamlit as st
import pandas as pd

st.title("NutriCare AI Diet Planner")

age = st.number_input("Enter Age")
weight = st.number_input("Enter Weight")
height = st.number_input("Enter Height")

goal = st.selectbox(
    "Select Goal",
    ["Weight Loss","Muscle Gain","Maintain Health"]
)

data = pd.read_csv("diet_data.csv")

if st.button("Generate Diet Plan"):

    breakfast = data[data["Type"]=="Breakfast"].sample(1)
    lunch = data[data["Type"]=="Lunch"].sample(1)
    dinner = data[data["Type"]=="Dinner"].sample(1)

    st.write("Breakfast:", breakfast["Food"].values[0])
    st.write("Lunch:", lunch["Food"].values[0])
    st.write("Dinner:", dinner["Food"].values[0])