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
            }
            .font-small-italic {
                 font-size: 16px;
                 font-style: italic;
                 line-height: 1pt;
            }
        </style>
        <body>
            <h1 class='font-big'>Dataset Preview</h1>
            <p class='font-small-italic'>(Not include : state, comments and Timestamp features)</p>
        <body>
        """
@st.cache_data
def load_data(data):
    df = pd.read_csv(data)
    df = df.iloc[:,1:]
    return df  

def run_ds_eda_app():
    st.write(temp,unsafe_allow_html=True)
    df = load_data("/survey.csv")
    
    # Data Cleansing for Null Value and Unnecessary Features
    columns_to_drop = ['state', 'comments', 'Timestamp']
    df_clean = df.drop(columns=[col for col in columns_to_drop if col in df])
    df_clean['work_interfere'].fillna(df_clean['work_interfere'].mode()[0], inplace=True)
    df_clean['self_employed'].fillna(df_clean['self_employed'].mode()[0], inplace=True)

    submenu = st.sidebar.selectbox("SubMenu",["Description","Visualization"])
    if submenu == "Description":
        st.dataframe(df)
        
        with st.expander("Dataset Summary"):
            buffer = io.StringIO()
            df_clean.info(buf=buffer)
            x=buffer.getvalue()
            st.text(x)

        with st.expander("Descriptive Summary"):
            st.dataframe(df_clean.describe(include='all').T)
        
        col1,col2,col3 = st.columns([2,2,2])
        with col1: 
            with st.expander("Country Distribution"):
                 st.dataframe(df_clean.groupby(by='Country').agg(Qty=('Country','count')).sort_values('Qty',ascending=False))
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
                with st.expander("Gender Distribution"):
                     st.dataframe(df_clean.groupby(by='Gender').agg(Qty=('Gender','count')).sort_values(by='Qty',ascending=False))

        with col3:
            with st.expander("Age Distribution"):
                 st.dataframe(df_clean.groupby(by='Age').agg(Qty=('Age','count')).sort_values(by='Qty',ascending=False))

        col1,col2 = st.columns([4,4])
        with col1: 
            with st.expander("Total Treatment Comparison based on Country"):
                 Treat=df_clean[df_clean['treatment'] == 'Yes'].groupby(by=['Country'], as_index=True)\
                                              .agg(Treatment = ('treatment', 'count'))\
                                              .sort_values(['Treatment'], ascending=False)\
                                              .head(10)
                 NoTreat=df_clean[df_clean['treatment'] == 'No'].groupby(by=['Country'], as_index=True)\
                                              .agg(NoTreatment = ('treatment', 'count'))\
                                              .sort_values(['NoTreatment'], ascending=False)\
                                              .head(10)                           
                 st.dataframe(Treat.merge(NoTreat,left_on='Country',right_on='Country'))
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
                with st.expander("Total Treatment Comparison based on Gender"):
                     Treat=df_clean[df_clean['treatment'] == 'Yes'].groupby(by=['Gender'], as_index=True)\
                                              .agg(Treatment = ('treatment', 'count'))\
                                              .sort_values(['Treatment'], ascending=False)\
                                              .head(10)
                     NoTreat=df_clean[df_clean['treatment'] == 'No'].groupby(by=['Gender'], as_index=True)\
                                              .agg(NoTreatment = ('treatment', 'count'))\
                                              .sort_values(['NoTreatment'], ascending=False)\
                                              .head(10)                           
                     st.dataframe(Treat.merge(NoTreat,left_on='Gender',right_on='Gender'))
        col1,col2 = st.columns([4,4])
        with col1: 
            with st.expander("Total Treatment Comparison based on Age"):
                 Treat=df_clean[df_clean['treatment'] == 'Yes'].groupby(by=['Age'], as_index=True)\
                                              .agg(Treatment = ('treatment', 'count'))\
                                              .sort_values(['Treatment'], ascending=False)\
                                              .head(10)
                 NoTreat=df_clean[df_clean['treatment'] == 'No'].groupby(by=['Age'], as_index=True)\
                                              .agg(NoTreatment = ('treatment', 'count'))\
                                              .sort_values(['NoTreatment'], ascending=False)\
                                              .head(10)                           
                 st.dataframe(Treat.merge(NoTreat,left_on='Age',right_on='Age'))
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
                with st.expander("Total Treatment Comparison based on Gender"):
                     Treat=df_clean[df_clean['treatment'] == 'Yes'].groupby(by=['Gender'], as_index=True)\
                                              .agg(Treatment = ('treatment', 'count'))\
                                              .sort_values(['Treatment'], ascending=False)\
                                              .head(10)
                     NoTreat=df_clean[df_clean['treatment'] == 'No'].groupby(by=['Gender'], as_index=True)\
                                              .agg(NoTreatment = ('treatment', 'count'))\
                                              .sort_values(['NoTreatment'], ascending=False)\
                                              .head(10)                           
                     st.dataframe(Treat.merge(NoTreat,left_on='Gender',right_on='Gender'))
        col1,col2 = st.columns([4,4])
        with col1: 
            with st.expander("Work Interfere Comparison based on Country"):
                 Often=df_clean[df_clean['work_interfere'] == 'Often'].groupby(by=['Country'], as_index=True)\
                                              .agg(Often = ('work_interfere', 'count'))\
                                              .sort_values(['Often'], ascending=False)\
                                              .head(10)
                 Rarely=df_clean[df_clean['work_interfere'] == 'Rarely'].groupby(by=['Country'], as_index=True)\
                                              .agg(Rarely = ('work_interfere', 'count'))\
                                              .sort_values(['Rarely'], ascending=False)\
                                              .head(10)
                 Never=df_clean[df_clean['work_interfere'] == 'Never'].groupby(by=['Country'], as_index=True)\
                                              .agg(Never = ('work_interfere', 'count'))\
                                              .sort_values(['Never'], ascending=False)\
                                              .head(10)
                 Sometimes=df_clean[df_clean['work_interfere'] == 'Sometimes'].groupby(by=['Country'], as_index=True)\
                                              .agg(Sometimes = ('work_interfere', 'count'))\
                                              .sort_values(['Sometimes'], ascending=False)\
                                              .head(10)                            
                 st.dataframe(pd.concat([Often,Rarely,Never,Sometimes],axis='columns'))
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
                with st.expander("Work Interfere Comparison based on Gender"):
                 Often=df_clean[df_clean['work_interfere'] == 'Often'].groupby(by=['Gender'], as_index=True)\
                                              .agg(Often = ('work_interfere', 'count'))\
                                              .sort_values(['Often'], ascending=False)\
                                              .head(10)
                 Rarely=df_clean[df_clean['work_interfere'] == 'Rarely'].groupby(by=['Gender'], as_index=True)\
                                              .agg(Rarely = ('work_interfere', 'count'))\
                                              .sort_values(['Rarely'], ascending=False)\
                                              .head(10)
                 Never=df_clean[df_clean['work_interfere'] == 'Never'].groupby(by=['Gender'], as_index=True)\
                                              .agg(Never = ('work_interfere', 'count'))\
                                              .sort_values(['Never'], ascending=False)\
                                              .head(10)
                 Sometimes=df_clean[df_clean['work_interfere'] == 'Sometimes'].groupby(by=['Gender'], as_index=True)\
                                              .agg(Sometimes = ('work_interfere', 'count'))\
                                              .sort_values(['Sometimes'], ascending=False)\
                                              .head(10)                            
                 st.dataframe(pd.concat([Often,Rarely,Never,Sometimes],axis='columns'))

    #elif submenu == "Visualization":
        #st.subheader("Data Visualization")

        # layouts
        #col1,col2 = st.columns([2,1])

        #with col1:
            #with st.expander("Dist Plot of Gender"):
                # fig = plt.figure()
                # sns.countplot(x=df['gender'])
                # st.pyplot(fig)

                #gen_df = df['gender'].value_counts().to_frame()
                #gen_df = gen_df.reset_index()
                #gen_df.columns = ['Gender Type', 'Counts']
                # st.dataframe(gen_df)

                #p1 = px.pie(gen_df, names='Gender Type', values='Counts')
                #st.plotly_chart(p1, use_container_width=True)
            
            # for Class Distribution
            #with st.expander("Dist Plot of Education"):
                #fig = plt.figure()
                #sns.countplot(x=df['education'])
                #st.pyplot(fig)

        #with col2:
            #with st.expander("Gender Distribution"):
                #st.dataframe(gen_df)

            #with st.expander("Education Distribution"):
                #st.dataframe(df['education'].value_counts().to_frame())

        #with st.expander("Frequency Distribution of Age"):
            #p2 = px.bar(age_viz, x='age_viz', y='values', text='label')
            #st.plotly_chart(p2)

        #with st.expander("Correlation Plot"):
            #columns = df.select_dtypes(include=['int64','float64']).columns.to_list()
            #corr_matrix = df[columns].corr()
            #fig = plt.figure(figsize=(20,10))
            #sns.heatmap(corr_matrix, annot=True, cmap="crest", linewidth=.5, annot_kws={"size":15})
            #st.pyplot(fig)
    #else:
        #st.write("Gorila Coklat")
