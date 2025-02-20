import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

user_animal_type = st.sidebar.selectbox("What is your Pet?",("Cat","Dog","Cow","Hamster"))

if user_animal_type == "Cat":
    pet_color = st.sidebar.text_area(label="What is the color of your Cat?",
    max_chars=10)
    
if user_animal_type == "Dog":
    pet_color = st.sidebar.text_area(label="What is the color of your Dog?",
    max_chars=10)
if user_animal_type == "Cow":
    pet_color = st.sidebar.text_area(label="What is the color of your Cow?",
    max_chars=10)
if user_animal_type == "Hamster":
    pet_color = st.sidebar.text_area(label="What is the color of your Hamster?",
    max_chars=10)

if pet_color:
    response = lch.generate_pet_name(user_animal_type, pet_color)
    st.text(response['pet_name'])


