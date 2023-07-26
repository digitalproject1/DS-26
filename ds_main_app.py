# Main Application
import streamlit as st
import streamlit.components.v1 as stc
import base64 

#import our app
from ds_dataprep_clean_app import run_ds_dataprep_clean_app
from ds_eda_app import run_ds_eda_app
#from ml_app import run_ml_app


home_temp = """
            <div style="background-color:#080366;padding:1px;border-radius:25px">
		    <h2 style="color:white;font-family:calibri;text-align:center;">FINAL PROJECT - DATA SCIENCE </h2>
            </div>
            """
desc_home_temp = """
                 <h4 style="color:white;font-family:calibri;font-size:14pt;text-align:left;">Team Collaboration : </h4>
                 """
desc_home2_temp = """
                 - Andi Muhammad Yusuf
                 - Anindya
                 - Tatag
                 - Erdiah 
                 """
about_temp = """
            <div style="background-color:#080366;padding:1px;border-radius:15px">
		    <h3 style="color:white;font-family:calibri;font-size:22pt;text-align:center;">Mental Health Treatment Prediction System </h3>
            </div>
            """
desc_about_temp = """
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

                <style type="text/css">
                    .left    { text-align: left;}
                    .right   { text-align: right;}
                    .center  { text-align: center;}
                    .justify-italic { text-align: justify;font-style:italic;line-height:1.2;}
                  ul.justify-bullet { text-align: justify;list-style-position: outside;line-height:1.3}
                  ol.justify-numbering { text-align: justify;list-style-position: outside;line-height:1.4}
                </style>

                <body>
                        <p> Data Source :
                            <a href="https://www.kaggle.com/code/numbrami/mental-health-treatment-prediction#Random-Forest-Classifier" title = "Menuju ke link data source"
                            >https://www.kaggle.com/code</a>
                        </p>
                    <h1 class='font-big'>About Dataset</h1>
                        <p class="justify-italic">"Mental Health in Tech Survey" is the dataset that was collected in 2014. This data is the result of the survey that measures 
                                                    attitude toward mental health and frequency of mental illness disorders in one of the tech workplace.</p>
                    <h1 class='font-big'>Research Question</h1>
                        <p class="left">The aim of our study is to answer the below research questions:</p>
                    <ul class="justify-bullet">
                        <li>How does the frequency of mental illness vary by geographic location ?</li>
                        <li>How does the attitude of the company toward mental health in the highest number of employees having mental disorder country ?</li>
                        <li>What are the strongest predictors of mental health illness or certain attitudes towards mental health in the workplace ?</li>
                    </ul>
                    <h1 class='font-big'>Feature</h1>
                        <p class="left">This dataset contains the following data :</p>
                    <ol class="justify-numbering">
                        <li>Timestamp</li>
                        <li>Age</li>
                        <li>Gender</li>
                        <li>Country</li>
                        <li>State : <i>If you live in the United States, which state or territory do you live in?</i></li>
                        <li>self_employed : <i>Are you self-employed?</i></li>
                        <li>family_history : <i>Do you have a family history of mental illness?</i></li>
                        <li>treatment : <i>Have you sought treatment for a mental health condition?</i></li>
                        <li>work_interfere : <i>If you have a mental health condition, do you feel that it interferes with your work?</i></li>
                        <li>no_employees : <i>How many employees does your company or organization have ?</i></li>
                        <li>remote_work : <i>Do you work remotely (outside of an office) at least 50% of the time ?</i></li>
                        <li>tech_company : <i>Is your employer primarily a tech company/organization ?</i></li>
                        <li>benefits : <i>Does your employer provide mental health benefits ?</i></li>
                        <li>care_options : <i>Do you know the options for mental health care your employer provides ?</i></li>
                        <li>wellness_program : <i>Has your employer ever discussed mental health as part of an employee wellness program ?</i></li>
                        <li>seek_help : <i>Does your employer provide resources to learn more about mental health issues and how to seek help ?</i></li>
                        <li>anonymity : <i>Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources ?</i></li>
                        <li>leave : <i>How easy is it for you to take medical leave for a mental health condition ?</i></li>
                        <li>mental_health_consequence : <i>Do you think that discussing a mental health issue with your employer would have negative consequences ?</i></li>
                        <li>phys_health_consequence : <i>Do you think that discussing a physical health issue with your employer would have negative consequences ?</i></li>
                        <li>coworkers : <i>Would you be willing to discuss a mental health issue with your coworkers ?</i></li>
                        <li>supervisor : <i>Would you be willing to discuss a mental health issue with your direct supervisor(s) ?</i></li>
                        <li>mental_health_interview : <i>Would you bring up a mental health issue with a potential employer in an interview ?</i></li>
                        <li>phys_health_interview : <i>Would you bring up a physical health issue with a potential employer in an interview ?</i></li>
                        <li>mental_vs_physical : <i>Do you feel that your employer takes mental health as seriously as physical health ?</i></li>
                        <li>obs_consequence : <i>Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace ?</i></li>
                        <li>comments : <i>Any additional notes or comments ?</i></li>
                    </ul>
                </body>

                 """

st.markdown(
    f"""
    <style>
    .sidebar.sidebar-content {{
        background-color: rgb(117 190 218 / 0.5);
        
    }}
    </style>
    """,
    unsafe_allow_html=True,
    )

st.markdown(
    f"""
    <style>
    .stApp{{
        background-color: #121111;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

def click_button_home():
    col1, mid, col2 = st.columns([1,1,25])
    with col1:
        st.image('/Data Privasi/archive/unicorn.png', width=60)
    with col2:
        st.write('Unicorn Team')
    
    st.write(home_temp,unsafe_allow_html=True)
    st.write(desc_home_temp,unsafe_allow_html=True)
    st.write(desc_home2_temp,unsafe_allow_html=True)
    
def click_button_about():
    st.write(about_temp,unsafe_allow_html=True)
    st.write(desc_about_temp,unsafe_allow_html=True)
    #st.write(desc_home2_temp,unsafe_allow_html=True)

def main():
    #st.title()
    #stc.html(about_temp)
    st.sidebar.button('HOME',use_container_width=True,on_click=click_button_home)      
    st.sidebar.button('ABOUT',use_container_width=True,on_click=click_button_about)
    st.sidebar.button('MENU',use_container_width=True)

    menu = ["Data Preprocessing & Cleansing","Exploratory Data Analysis","Machine Learning"]
    choice = st.sidebar.selectbox("select", menu)

    if choice == "Data Preprocessing & Cleansing":
        st.subheader("Data Preprocessing and Cleansing Result")
        run_ds_dataprep_clean_app()
    elif choice == "Exploratory Data Analysis":
        st.subheader("Exploratory Data Analysis")
        run_ds_eda_app()
    #elif choice == "Machine Learning":
        #run_ml_app()
    
if __name__ == '__main__':
    main()