import streamlit as st
import pandas as pd
import pickle
from tensorflow.keras.models import load_model #type: ignore
import sqlite3

scaler_loaded = pickle.load(open('scaler.pkl', 'rb'))
model_loaded = load_model('placement_ann_model.h5')

conn = sqlite3.connect('placement_prediction.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    CGPA REAL,
    Internships INTEGER,
    Projects INTEGER,
    Workshops INTEGER,
    Aptitude INTEGER,
    SoftSkills REAL,
    Extracurricular INTEGER,
    PlacementTraining INTEGER,
    SSC INTEGER,
    HSC INTEGER,
    Probatility REAL,
    Result TEXT
    )
""")
conn.commit()

st.title("Student Placement Prediction System")
st.write("Enter student details to predict placement status")

CGPA = st.number_input("CGPA", 0.0, 10.0, 3.0)
Internships = st.number_input("Number of Internships", 0)
Projects = st.number_input("Number of Projects", 0)
Workshops = st.number_input("Workshops/Certifications", 0)
Aptitude = st.number_input("Aptitude Test Score", 0, 100)
SoftSkills = st.number_input("Soft Skills Ratings", 0.0, 5.0)
Extracurricular = st.selectbox("Extracurricular Activities", ["No", "Yes"])
PlacementTraining = st.selectbox("Placement Training", ["No", "Yes"])
SSC = st.number_input("SSC Marks", 0, 100)
HSC = st.number_input("HSC Marks", 0, 100)

Extracurricular = 1 if Extracurricular == "Yes" else 0
PlacementTraining = 1 if PlacementTraining == "Yes" else 0

if st.button("Predict Placement"):
    input_data = pd.DataFrame({
        'CGPA': [CGPA],             
        'Internships': [Internships],
        'Projects': [Projects],
        'Workshops/Certifications': [Workshops],
        'AptitudeTestScore': [Aptitude],
        'SoftSkillsRating': [SoftSkills],
        'ExtracurricularActivities': [Extracurricular],
        'PlacementTraining': [PlacementTraining],
        'SSC_Marks': [SSC],
        'HSC_Marks': [HSC]
    })

    input_scaled = scaler_loaded.transform(input_data)

    prediction = model_loaded.predict(input_scaled)
    probability = prediction[0][0]

    result = "Placed" if probability > 0.5 else "Not Placed"

    cursor.execute("""
    INSERT INTO predictions 
        (CGPA, Internships, Projects, Workshops, Aptitude, SoftSkills, Extracurricular, PlacementTraining, SSC, HSC, Probatility, Result)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (CGPA, Internships, Projects, Workshops, Aptitude, SoftSkills, Extracurricular, PlacementTraining, SSC, HSC, float(probability), result))
    conn.commit()

    if result == "Placed":
        st.success(f"Placed (Probability: {probability:.2f})")
    else:
        st.error(f"Not Placed (Probability: {probability:.2f})")

st.subheader("Prediction History")

if st.button("Show History"):
    history = pd.read_sql_query("SELECT * FROM predictions", conn)
    st.dataframe(history)