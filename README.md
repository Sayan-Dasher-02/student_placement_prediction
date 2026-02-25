# 🧠 Student Placement Prediction Web App

This project is a **Streamlit-based web application** that predicts whether a student is likely to get **placed** based on academic and extracurricular data.  
It uses a trained **Deep Learning model** built with **TensorFlow/Keras** and preprocessing with **Scikit-learn**.

***

## 🚀 Features

- 🎛️ Interactive Streamlit UI for student input  
- ⚡ Real-time placement probability prediction  
- 🤖 Uses pre-trained model and scaler for inference  
- ☁️ Easy to deploy locally or on cloud platforms (e.g., Streamlit Cloud, Heroku)

***

## 📁 Project Structure

Student-Placement-Prediction/
│
├── main.py # Streamlit app code (rename to app.py for standard deployment)
├── experiment.ipynb # Notebook for model training & experiments
├── placementdata.csv # Dataset used for training
├── scaler.pkl # Scaler used for numerical features
└── placementannmodel.h5 # Trained TensorFlow model

***

## 🧠 Model Overview

- **Framework:** TensorFlow / Keras  
- **Preprocessing:** StandardScaler for numerical features  
- **Target:** `PlacementStatus` → (Placed / NotPlaced)  
- **Inputs:**  
  `CGPA`, `Internships`, `Projects`, `WorkshopsCertifications`, `AptitudeTestScore`,  
  `SoftSkillsRating`, `ExtracurricularActivities`, `PlacementTraining`, `SSCMarks`, `HSCMarks`

***

## 🧩 Requirements

Install dependencies:

```bash
pip install streamlit tensorflow scikit-learn pandas numpy sqlite3
```

## ⚙️ Setup Instructions

1. Ensure files are in the same directory: `main.py` (or `app.py`), `experiment.ipynb`, `placementdata.csv`, `scaler.pkl`, `placementannmodel.h5`.
2. Run the app:

```bash
cd student_placement_prediction
Streamlit run main.py
```

The app opens in your browser at http://localhost:8501.

## 🧪 How to Use

- Enter student details using sliders and dropdowns.
- Click **Predict Placement**.
- View probability and result (Placed/Not Placed).
- Check prediction history stored in SQLite DB 

## 🧰 Troubleshooting

- ⚠️ Missing files: Add `scaler.pkl` and `placementannmodel.h5` next to `main.py`
- 🔁 Retrain: Run `experiment.ipynb` to regenerate model/scaler
- ⚙️ Scaler mismatch: Refit scaler on same features from `placementdata.csv` 

## 📜 License

MIT License. Use, modify freely with attribution.
