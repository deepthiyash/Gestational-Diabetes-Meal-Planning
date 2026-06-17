import streamlit as st
import random
from meal_data import *

st.set_page_config(
    page_title="Gestational Diabetes Meal Planner",
    page_icon="🥗"
)

st.title("🥗 Gestational Diabetes Meal Planner")
st.warning("Educational guidance only. Not medical advice.")

age = st.number_input("Age", 18, 50, 30)
weight = st.number_input("Weight (kg)", 40, 150, 70)
height = st.number_input("Height (cm)", 140, 200, 160)

trimester = st.selectbox("Trimester", ["First", "Second", "Third"])

fasting = st.number_input("Fasting Blood Sugar", 50, 250, 90)
post_meal = st.number_input("Post-meal Blood Sugar", 50, 350, 120)

if st.button("Generate Meal Plan"):
    bmi = round(weight / ((height / 100) ** 2), 1)
    calories = int(weight * 30)

    st.subheader("Assessment")
    st.write(f"BMI: {bmi}")
    st.write(f"Estimated Daily Calories: {calories}")

    if fasting > 95:
        st.warning("Fasting glucose is above target. Please discuss with your healthcare provider.")

    if post_meal > 140:
        st.warning("Post-meal glucose is above target. Please discuss with your healthcare provider.")

    st.subheader("Meal Plan")
    st.write(f"Breakfast: {random.choice(VEG_BREAKFAST)}")
    st.write(f"Morning Snack: {random.choice(SNACKS)}")
    st.write(f"Lunch: {random.choice(VEG_LUNCH)}")
    st.write(f"Evening Snack: {random.choice(SNACKS)}")
    st.write(f"Dinner: {random.choice(VEG_DINNER)}")

    st.subheader("Foods To Limit")
    st.write("""
    - Sugary drinks
    - Fruit juices
    - White bread
    - Bakery items
    - Excess sweets
    """)
