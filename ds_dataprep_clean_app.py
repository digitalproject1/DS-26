import streamlit as st
import pandas as pd

temp_1 = """
        <style>
            h1 {
                font-size: 18px;
                color: white;
            }
            .font-big {
                 font-size: large;
            }
            .font-small {
                 font-size: middle;
            }
        </style>
        <body>
            <h1 class='font-big'>Dataset Preview</h1>
        <body>
        """
temp_2 = """
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
            <h1 class='font-big'>Data Visualization</h1>
        <body>
        """
@st.cache_data
def load_data(data):
    df = pd.read_csv(data)
    df = df.iloc[:,1:]
    return df  

def run_ds_dataprep_clean_app():
    df = load_data("/Data Privasi/Modul Programming/Python/Final Project/Code/survey.csv")
    
    # Data Cleansing for Null Value, Unnecessary Features 
    columns_to_drop = ['state', 'comments', 'Timestamp']
    df_clean = df.drop(columns=[col for col in columns_to_drop if col in df])
    df_clean['work_interfere'].fillna(df_clean['work_interfere'].mode()[0], inplace=True)
    df_clean['self_employed'].fillna(df_clean['self_employed'].mode()[0], inplace=True)
    
    def organizer_gender():
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
    

    submenu = st.sidebar.selectbox("SubMenu",["Visualization","Description"])
    organizer_gender()
    if submenu == "Visualization":
        st.write(temp_2,unsafe_allow_html=True)
        
        df_clean_age = df_clean[(df['Age'] >= 17) & (df_clean['Age'] <= 99)]
        work_interfere_b=df['work_interfere'].value_counts()
        work_interfere_a=df_clean['work_interfere'].value_counts()
        self_employed_b=df['self_employed'].value_counts()
        self_employed_a=df_clean['self_employed'].value_counts()

        col1,col2=st.columns([2,2])
        
        col1.write("Data Plot Work Interfere Before Cleansing")
        col1.bar_chart(work_interfere_b)
        col1.write("Data Plot Self Employed Before Cleansing")
        col1.bar_chart(self_employed_b)
        col1.write('Data Plot Genders Before Cleansing and New Categorizing')   
        col1.bar_chart(df['Gender'].value_counts())    
        col1.write('Data Plot Age Before Age Restriction')  
        col1.bar_chart(df['Age'].value_counts())    
                
        col2.write("Data Plot Work Interfere After Cleansing")
        col2.bar_chart(work_interfere_a) 
        col2.write("Data Plot Self Employed After Cleansing")
        col2.bar_chart(self_employed_a)
        col2.write('Data Plot Genders After cleansing and New Categorizing')   
        col2.bar_chart(df_clean['Gender'].value_counts())
        col2.write('Data Plot Age After Age Restriction')   
        col2.bar_chart(df_clean_age['Age'].value_counts())


    elif submenu == "Description":
        st.write(temp_1,unsafe_allow_html=True)
        st.dataframe(df)
        col1,col2=st.columns([2,2])
        with col1:          
            with st.expander("Check Data Null Value Before Cleansing"):
                st.dataframe(df.isnull().sum())
            with st.expander("Check Data Unique Gender Before Cleansing"):
                 st.dataframe(df.groupby(by='Gender').agg(Qty=('Gender','count')).sort_values(by='Qty',ascending=False))
                 st.text('%s%s' % (df['Gender'].nunique(),' data')) 
            with st.expander("Check Data Unique Age Before Cleansing"):
                 st.dataframe(df.groupby(by='Age').agg(Qty=('Age','count')).sort_values(by='Qty',ascending=False))
                 st.text('%s%s' % (df['Age'].nunique(),' data'))
        with col2:
            with st.expander("Check Data Null Value After Cleansing"):
                st.dataframe(df_clean.isnull().sum())
            with st.expander("Check Data Unique Gender After Cleansing"):
                 st.dataframe(df_clean.groupby(by='Gender').agg(Qty=('Gender','count')).sort_values(by='Qty',ascending=False))
                 st.text('%s%s' % (df_clean['Gender'].nunique(),' data'))
            with st.expander("Check Data Unique Age After Cleansing"):
                 #age restriction
                 df_clean_age = df_clean[(df['Age'] >= 17) & (df_clean['Age'] <= 99)]

                 st.dataframe(df_clean_age.groupby(by='Age').agg(Qty=('Age','count')).sort_values(by='Qty',ascending=False))
                 st.text('%s%s' % (df_clean_age['Age'].nunique(),' data'))
