import streamlit as st

# Define the input fields
age = st.number_input('Age in years', min_value=1, max_value=120, value=25)
num_sexual_partners = st.number_input('Number of sexual partners', min_value=0, max_value=100, value=1)
first_sexual_intercourse = st.number_input('Age at first sexual intercourse', min_value=1, max_value=120, value=18)
num_pregnancies = st.number_input('Number of pregnancies', min_value=0, max_value=100, value=0)
smoking = st.selectbox('Do you smoke?', ['Yes', 'No'])
smoking_years = st.number_input('Number of years smoking', min_value=0, max_value=100, value=0)
hormonal_contraceptives = st.selectbox('Do you use hormonal contraceptives?', ['Yes', 'No'])
hormonal_contraceptives_years = st.number_input('Number of years using hormonal contraceptives', min_value=0, max_value=100, value=0)
iud = st.selectbox('Do you use an intrauterine device (IUD)?', ['Yes', 'No'])
iud_years = st.number_input('Number of years using an IUD', min_value=0, max_value=100, value=0)
std = st.selectbox('Have you ever had a sexually transmitted disease (STD)?', ['Yes', 'No'])
num_std_diagnoses = st.number_input('Number of STD diagnoses', min_value=0, max_value=100, value=0)
time_since_first_std = st.number_input('Time since first STD diagnosis (in years)', min_value=0, max_value=100, value=0)
time_since_last_std = st.number_input('Time since last STD diagnosis (in years)', min_value=0, max_value=100, value=0)

# Define the submit button
if st.button('Submit'):
    # Calculate the risk percentage using a simple algorithm
    risk_percentage = 0
    if age < 18:
        risk_percentage += 5
    if num_sexual_partners > 3:
        risk_percentage += 10
    if first_sexual_intercourse < 16:
        risk_percentage += 5
    if num_pregnancies == 0:
        risk_percentage += 5
    if smoking == 'Yes':
        risk_percentage += 10
    if smoking_years > 10:
        risk_percentage += 10
    if hormonal_contraceptives == 'Yes':
        risk_percentage += 5
    if hormonal_contraceptives_years > 5:
        risk_percentage += 5
    if iud == 'Yes':
        risk_percentage += 5
    if iud_years > 5:
        risk_percentage += 5
    if std == 'Yes':
        risk_percentage += 10
    if num_std_diagnoses > 1:
        risk_percentage += 10
    if time_since_first_std < 5:
        risk_percentage += 5
    if time_since_last_std < 5:
        risk_percentage += 5

    # Display the risk percentage to the user
    st.write('Your risk of developing cervical cancer is:', risk_percentage, '%')
