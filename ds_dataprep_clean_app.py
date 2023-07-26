from lib2to3.pgen2.pgen import DFAState
import streamlit as st
import pandas as pd
import numpy as np
import io

# import visualization package
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px

temp = """
        <style>
            h1 {
                font-size: 18px;
                color: white;
            }
            .font-big {
                 font-size: large;
                 font-
            }
            .font-small {
                 font-size: middle;
            }
        </style>
        <body>
            <h1 class='font-big'>Dataset Preview</h1>
        <body>
        """
@st.cache_data
def load_data(data):
    df = pd.read_csv(data)
    df = df.iloc[:,1:]
    return df  

def run_ds_dataprep_clean_app():
    st.write(temp,unsafe_allow_html=True)
    df = load_data("ds-26/main/survey.csv")
    
    # Data Cleansing for Null Value and Unnecessary Features
    columns_to_drop = ['state', 'comments', 'Timestamp']
    df_clean = df.drop(columns=[col for col in columns_to_drop if col in df])
    df_clean['work_interfere'].fillna(df_clean['work_interfere'].mode()[0], inplace=True)
    df_clean['self_employed'].fillna(df_clean['self_employed'].mode()[0], inplace=True)

    #submenu = st.sidebar.selectbox("SubMenu",["Description","Visualization"])
    #if submenu == "Description":
    st.dataframe(df)
    col1,col2=st.columns([2,2])
    with col1:          
        with st.expander("Check Data Before Cleansing"):
             st.dataframe(df.isnull().sum())
    with col2:
        with st.expander("Check Data After Cleansing"):
             st.dataframe(df_clean.isnull().sum())

    col1,col2= st.columns([2,2])
    with col1: 
            with st.expander("Check Data Unique (Gender)"):
                 st.dataframe(df_clean.groupby(by='Gender').agg(Qty=('Gender','count')).sort_values(by='Qty',ascending=False))
    with col2: 
            organize_genders = {
                    'Male ': 'Male',
                    'male': 'Male',
                    'M': 'Male',
                    'm': 'Male',
                    'Male': 'Male',
                    'Cis Male': 'Male',
                    'Man': 'Male',
                    'cis male': 'Male',
                    'Mail': 'Male',
                    'Male-ish': 'Male',
                    'Male (CIS)': 'Male',
                    'Cis Man': 'Male',
                    'msle': 'Male',
                    'Malr': 'Male',
                    'Mal': 'Male',
                    'maile': 'Male',
                    'Make': 'Male',
                    'Female ': 'Female',
                    'female': 'Female',
                    'F': 'Female',
                    'f': 'Female',
                    'Woman': 'Female',
                    'Female': 'Female',
                    'femail': 'Female',
                    'Cis Female': 'Female',
                    'cis-female/femme': 'Female',
                    'Femake': 'Female',
                    'Female (cis)': 'Female',
                    'woman': 'Female',
                    'Female (trans)': 'Other',
                    'queer/she/they': 'Other',
                    'non-binary': 'Other',
                    'fluid': 'Other',
                    'queer': 'Other',
                    'Androgyne': 'Other',
                    'Trans-female': 'Other',
                    'male leaning androgynous': 'Other',
                    'Agender': 'Other',
                    'A little about you': 'Other',
                    'Nah': 'Other',
                    'All': 'Other',
                    'ostensibly male, unsure what that really means': 'Other',
                    'Genderqueer': 'Other',
                    'Enby': 'Other',
                    'p': 'Other',
                    'Neuter': 'Other',
                    'something kinda male?': 'Other',
                    'Guy (-ish) ^_^': 'Other',
                    'Trans woman': 'Other'
                    }               
            df_clean['Gender'].replace(organize_genders,inplace=True)
            with st.expander("Check Data Gender After Cleansing"):
                 st.dataframe(df_clean.groupby(by='Gender').agg(Qty=('Gender','count')).sort_values(by='Qty',ascending=False))


