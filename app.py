import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('migraine_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title of the app
st.title("Migraine Type Prediction")

# Create form for user input
with st.form("prediction_form"):
    st.header("Enter the following features:")
    
    age = st.number_input("Age (years)", min_value=0, max_value=100, value=25)
    duration = st.number_input("Duration (days)", min_value=0.0, max_value=100.0, value=0.0)
    frequency = st.number_input("Frequency of episodes per month", min_value=0, max_value=365, value=0)
    location = st.number_input("Location 0 : None 1 : Unilateral 2 : Bilateral", min_value=0, max_value=10, value=0)
    character = st.number_input("Character", min_value=0, max_value=10, value=0)
    intensity = st.number_input("Intensity", min_value=0, max_value=10, value=0)
    nausea = st.number_input("Nausea", min_value=0, max_value=10, value=0)
    vomit = st.number_input("Vomit", min_value=0, max_value=10, value=0)
    phonophobia = st.number_input("Phonophobia", min_value=0, max_value=10, value=0)
    photophobia = st.number_input("Photophobia", min_value=0, max_value=10, value=0)
    visual = st.number_input("Visual", min_value=0, max_value=10, value=0)
    sensory = st.number_input("Sensory", min_value=0, max_value=10, value=0)
    dysphasia = st.number_input("Dysphasia", min_value=0, max_value=10, value=0)
    dysarthria = st.number_input("Dysarthria", min_value=0, max_value=10, value=0)
    vertigo = st.number_input("Vertigo", min_value=0, max_value=10, value=0)
    tinnitus = st.number_input("Tinnitus", min_value=0, max_value=10, value=0)
    hypoacusis = st.number_input("Hypoacusis", min_value=0, max_value=10, value=0)
    diplopia = st.number_input("Diplopia", min_value=0, max_value=10, value=0)
    defect = st.number_input("Defect", min_value=0, max_value=10, value=0)
    ataxia = st.number_input("Ataxia", min_value=0, max_value=10, value=0)
    conscience = st.number_input("Conscience", min_value=0, max_value=10, value=0)
    paresthesia = st.number_input("Paresthesia", min_value=0, max_value=10, value=0)
    dpf = st.number_input("DPF", min_value=0.0, max_value=10.0, value=0.0)
    
    # Submit button
    submitted = st.form_submit_button("Predict")
    
    if submitted:
        # Make prediction
        features = np.array([[age, duration, frequency, location, character, intensity, nausea, vomit, 
                              phonophobia, photophobia, visual, sensory, dysphasia, dysarthria, vertigo, 
                              tinnitus, hypoacusis, diplopia, defect, ataxia, conscience, paresthesia, dpf]])
        prediction = model.predict(features)
        st.subheader(f"The predicted type of migraine is: {prediction[0]}")

