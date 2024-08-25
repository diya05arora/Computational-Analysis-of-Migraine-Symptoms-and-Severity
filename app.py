import streamlit as st
import pickle
import numpy as np


# Load the trained model
with open('migraine_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f1:
    scaler = pickle.load(f1)


# Title of the app
st.title("Migraine Type Prediction")

# Create form for user input
with st.form("prediction_form"):
    st.header("Enter the following features:")
    
    age = st.number_input("Age (years)", min_value=0, max_value=100, value=25)
    duration = st.number_input("Duration of symptoms in last episode (days)", min_value=0, max_value=3, value=0)
    frequency = st.number_input("Frequency of episodes per month", min_value=0, max_value=10, value=0)
    location = st.number_input("Location 0 : None, 1 : Unilateral, 2 : Bilateral", min_value=0, max_value=2, value=0)
    character = st.number_input("Character 0 : None, 1 : Throbbing, 2 : Constant", min_value=0, max_value=2, value=0)
    intensity = st.number_input("Pain Intensity 0 : None, 1 : Mild, 2 : Medium, 3 : Severe", min_value=0, max_value=3, value=0)
    nausea = st.number_input("Nausea 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    vomit = st.number_input("Vomit 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    phonophobia = st.number_input("Phonophobia 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    photophobia = st.number_input("Photophobia 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    visual = st.number_input("Visual 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    sensory = st.number_input("Sensory 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    dysphasia = st.number_input("Dysphasia 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    dysarthria = st.number_input("Dysarthria 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    vertigo = st.number_input("Vertigo 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    tinnitus = st.number_input("Tinnitus 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    hypoacusis = st.number_input("Hypoacusis 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    diplopia = st.number_input("Diplopia 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    defect = st.number_input("Defect 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    ataxia = st.number_input("Ataxia 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    conscience = st.number_input("Conscience 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    paresthesia = st.number_input("Paresthesia 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
    dpf = st.number_input("DPF 0 : Yes, 1 : No", min_value=0, max_value=1, value=0)
   
    
 
    submitted = st.form_submit_button("Predict")
    
    if submitted:
        features = np.array([[age, duration, frequency, location, character, intensity, nausea, vomit, 
                              phonophobia, photophobia, visual, sensory, dysphasia, dysarthria, vertigo, 
                              tinnitus, hypoacusis, diplopia, defect, ataxia, conscience, paresthesia, dpf]])
        
        features = scaler.transform(features)

        prediction = model.predict(features)
        st.subheader(f"The predicted type of migraine is: {prediction[0]}")

