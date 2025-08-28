# app.py
import os
import pickle
import numpy as np
import pandas as pd
import streamlit as st

# --- Load model ---
MODEL_PATH = os.path.join("model", "model.pkl")
@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

st.set_page_config(page_title="Demo Predictor", page_icon="🤖", layout="centered")
st.title("🤖 Simple Predictor Dashboard")
st.caption("Loads model/model.pkl and predicts from two features")

# Sidebar
st.sidebar.header("Input features")
f1 = st.sidebar.number_input("feature1", value=0.10, step=0.05, format="%.4f")
f2 = st.sidebar.number_input("feature2", value=0.20, step=0.05, format="%.4f")

# Predict button
model = load_model()
if st.button("Predict"):
    X = np.array([[f1, f2]])
    pred = model.predict(X)[0]
    proba = getattr(model, "predict_proba", lambda x: None)(X)
    st.success(f"Prediction: **{int(pred)}**")
    if proba is not None:
        st.write("Class probabilities:", pd.Series(proba[0]).rename("prob").to_frame())

# Quick demo chart
st.subheader("Feature sweep")
f1_vals = np.linspace(-2, 2, 41)
X_grid = np.column_stack([f1_vals, np.full_like(f1_vals, f2)])
y_hat = model.predict(X_grid)
st.line_chart(pd.DataFrame({"feature1": f1_vals, "prediction": y_hat}).set_index("feature1"))
