import streamlit as st
import pickle 
import numpy as np

with open("model.pkl","rb") as p:
    model=pickle.load(p)
    
st.title("Sales Prediction Application")

st.write("Please enter your advertisement invest in each to predict sales")

TV =st.number_input("Advertising investment in TV",min_value=0.0,format="%.2f")  
RADIO =st.number_input("Advertising investment in RADIO",min_value=0.0,format="%.2f") 
NEWSPAPER =st.number_input("Advertising investment in NEWSPAPER",min_value=0.0,format="%.2f")    
   
if st.button("Predict Sales"):
    features=np.array([[TV,RADIO,NEWSPAPER]])
    predictions=model.predict(features)[0]
    st.success(f"predicted Sales: {predictions :.2f}")
  
