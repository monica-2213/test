import streamlit as st
import pandas as pd
import joblib

# Load the machine learning model
model = joblib.load('cervical_cancer_prediction.joblib')

# Create the web app
st.title('Cervical Cancer Expert System')
st.write('This expert system predicts the likelihood of cervical cancer based on personal information and medical history.')

# Ask for the user's personal information
age = st.number_input('Age:', min_value=0, max_value=120, value=25, step=1)
sexual_partners = st.slider('Number of sexual partners:', 0, 50, 1)
first_sexual_intercourse = st.number_input('Age at first sexual intercourse:', min_value=0, max_value=120, value=18, step=1)
pregnancies = st.slider('Number of pregnancies:', 0, 20, 1)
smoking = st.selectbox('Do you smoke?', ['Yes', 'No'])
if smoking == 'Yes':
    smoking_years = st.slider('Number of years smoked:', 0, 60, 10)
    smoking_packs = st.slider('Number of packs smoked per year:', 0, 60, 10)
else:
    smoking_years = 0
    smoking_packs = 0
contraceptives = st.selectbox('Do you use hormonal contraceptives?', ['Yes', 'No'])
if contraceptives == 'Yes':
    contraceptive_years = st.slider('Number of years using hormonal contraceptives:', 0, 50, 10)
else:
    contraceptive_years = 0
iud = st.selectbox('Do you use an intrauterine device (IUD)?', ['Yes', 'No'])
if iud == 'Yes':
    iud_years = st.slider('Number of years using an IUD:', 0, 50, 10)
else:
    iud_years = 0
stds = st.selectbox('Have you had any sexually transmitted diseases?', ['Yes', 'No'])
if stds == 'Yes':
    stds_num = st.slider('How many sexually transmitted diseases have you had?', 0, 5)
    stds_cond = st.checkbox('Other sexually transmitted disease')
    stds_cervical_cond = st.checkbox('Cervical Condylomatosis')
    stds_vaginal_cond = st.checkbox('Vaginal Condylomatosis')
    stds_vulvo_cond = st.checkbox('Vulvo-perineal Condylomatosis')
    stds_syphilis = st.checkbox('Syphilis')
    stds_pid = st.checkbox('Pelvic Inflammatory Disease')
    stds_herpes = st.checkbox('Genital Herpes')
    stds_molluscum = st.checkbox('Molluscum Contagiosum')
    stds_aids = st.checkbox('AIDS')
    stds_hiv = st.checkbox('HIV')
    stds_hepatitis = st.checkbox('Hepatitis B')
    stds_hpv = st.checkbox('HPV')
    stds_diagnosis = st.slider('How many diagnoses of sexually transmitted diseases have you had?', 0, 5)
else:
    stds_num = 0
    stds_cond = False
    stds_cervical_cond = False
    stds_vaginal_cond = False
    stds_vulvo_cond = False
    stds_syphilis = False
    stds_pid = False
    stds_herpes = False
    stds_molluscum = False
    stds_aids = False
    stds_hiv = False
    stds_hepatitis = False
    stds_hpv = False
    stds_diagnosis = 0

# Make the prediction
predict_button = st.button('Predict')
if predict_button:
    # Convert the inputs to a DataFrame
    input_data = pd.DataFrame({
        'Age': [age],
        'Number of sexual partners': [sexual_partners],
        'Age at first sexual intercourse': [first_sexual_intercourse],
        'Number of pregnancies': [pregnancies],
        'Smokes': [smoking],
        'Smokes (years)': [smoking_years],
        'Smokes (packs/year)': [smoking_packs],
        'Hormonal Contraceptives': [contraceptives],
        'Hormonal Contraceptives (years)': [contraceptive_years],
        'IUD': [iud],
        'IUD (years)': [iud_years],
        'STDs': [stds],
        'STDs (number)': [stds_num],
        'STDs:condylomatosis': [stds_cond],
        'STDs:cervical condylomatosis': [stds_cervical_cond],
        'STDs:vaginal condylomatosis': [stds_vaginal_cond],
        'STDs:vulvo-perineal condylomatosis': [stds_vulvo_cond],
        'STDs:syphilis': [stds_syphilis],
        'STDs:pelvic inflammatory disease': [stds_pid],
        'STDs:genital herpes': [stds_herpes],
        'STDs:molluscum contagiosum': [stds_molluscum],
        'STDs:AIDS': [stds_aids],
        'STDs:HIV': [stds_hiv],
        'STDs:Hepatitis B': [stds_hepatitis],
        'STDs:HPV': [stds_hpv],
        'STDs: Number of diagnosis': [stds_diagnosis]
    })

    # Make the prediction
    prediction = model.predict(input_data)

    # Display the prediction
    if prediction[0] == 0:
        st.write('Based on the input data, you are likely **not** to have cervical cancer.')
    else:
        st.write('Based on the input data, you are likely to have cervical cancer. Please consult a medical professional for further evaluation.')
