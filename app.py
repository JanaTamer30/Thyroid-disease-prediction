import streamlit as st
import pandas as pd
import pickle



# Load the trained machine learning model
model=pickle.load(open(r'C:\Users\samar\Desktop\Thyroid\thyroid.sav','rb'))

st.title("Thyroid disease prediction app")
st.info('Application for Thyroid disease prediction')

# Sidebar for feature selection
st.sidebar.header('Selection Bar')

# User inputs
Age=st.text_input('age')
Sex=st.text_input('sex')
Thyroid_Stimulating_Hormone=st.text_input('TSH')
Triiodothyronine =st.text_input('T3')
Total_Thyroxine =st.text_input('TT4')
Thyroxine_Utilization_Rate =st.text_input('T4U')
Free_Thyroxine_Index =st.text_input('FTI')
T3_TT4_ratio =st.text_input('T3_TT4_ratio')


# Create a dataframe with the user input
df = pd.DataFrame({
    'Age': [Age],
    'Sex': [Sex],
    'Thyroid_Stimulating_Hormone': [Thyroid_Stimulating_Hormone],
    'Triiodothyronine': [Triiodothyronine],
    'Total_Thyroxine': [Total_Thyroxine],
    'Thyroxine_Utilization_Rate': [Thyroxine_Utilization_Rate],
    'T3_TT4_ratio': [T3_TT4_ratio],
    'Free_Thyroxine_Index': [Free_Thyroxine_Index]
    },index=[0])

Con=st.sidebar.button('confirm')

if Con:
    result=model.predict(df)
    st.write(result)