import streamlit as st
import pandas as pd

# Load the dataset
data_url = 'https://datahub.io/machine-learning/cervical-cancer/r/cervical-cancer_csv.csv'
df = pd.read_csv(data_url)

# Define the rules library
rules = {
    'age': {
        'rule': lambda x: x >= 18 and x <= 84,
        'error_message': 'Please enter a valid age between 18 and 84'
    },
    'num_sexual_partners': {
        'rule': lambda x: x >= 0,
        'error_message': 'Please enter a valid number of sexual partners'
    },
    'first_sexual_intercourse': {
        'rule': lambda x: x >= 10 and x <= 32,
        'error_message': 'Please enter a valid age of first sexual intercourse between 10 and 32'
    },
    'num_pregnancies': {
        'rule': lambda x: x >= 0,
        'error_message': 'Please enter a valid number of pregnancies'
    },
    'smoke': {
        'rule': lambda x: x in ['Yes', 'No'],
        'error_message': 'Please enter either Yes or No for smoking'
    },
    'smoking_years': {
        'rule': lambda x: x >= 0,
        'error_message': 'Please enter a valid number of smoking years'
    },
    'hormonal_contraceptives': {
        'rule': lambda x: x in ['Yes', 'No'],
        'error_message': 'Please enter either Yes or No for hormonal contraceptives'
    },
    'hormonal_contraceptives_years': {
        'rule': lambda x: x >= 0,
        'error_message': 'Please enter a valid number of hormonal contraceptive years'
    },
    'iud': {
        'rule': lambda x: x in ['Yes', 'No'],
        'error_message': 'Please enter either Yes or No for intrauterine device (IUD)'
    },
    'iud_years': {
        'rule': lambda x: x >= 0,
        'error_message': 'Please enter a valid number of intrauterine device (IUD) years'
    },
    'stds': {
        'rule': lambda x: x in ['Yes', 'No'],
        'error_message': 'Please enter either Yes or No for sexually transmitted diseases (STDs)'
    },
    'num_stds': {
        'rule': lambda x: x >= 0,
        'error_message': 'Please enter a valid number of sexually transmitted disease diagnoses'
    },
    'time_since_first_std': {
        'rule': lambda x: x >= 0,
        'error_message': 'Please enter a valid time (in years) since first STD diagnosis'
    },
    'time_since_last_std': {
        'rule': lambda x: x >= 0,
        'error_message': 'Please enter a valid time (in years) since last STD diagnosis'
    },
}

def cervical_cancer_rules(age, num_sexual_partners, first_sexual_intercourse, num_pregnancies, smoking, smoking_years, hormonal_contraceptives, hormonal_contraceptives_years, iud, iud_years, std, num_std_diagnoses, time_since_first_std, time_since_last_std):
    
    # Rule 1: Age over 21 years old increases risk
    if age > 21:
        risk += 1
    
    # Rule 2: Having more than 3 sexual partners increases risk
    if num_sexual_partners > 3:
        risk += 1
    
    # Rule 3: Early age at first sexual intercourse (less than 16 years old) increases risk
    if first_sexual_intercourse < 16:
        risk += 1
    
    # Rule 4: Number of pregnancies over 3 increases risk
    if num_pregnancies > 3:
        risk += 1
    
    # Rule 5: Smoking increases risk
    if smoking == 'Yes':
        risk += 1
        if smoking_years >= 15:
            risk += 1
    
    # Rule 6: Use of hormonal contraceptives increases risk
    if hormonal_contraceptives == 'Yes':
        risk += 1
        if hormonal_contraceptives_years >= 5:
            risk += 1
    
    # Rule 7: Use of an IUD decreases risk
    if iud == 'Yes':
        risk -= 1
        if iud_years >= 3:
            risk -= 1
    
    # Rule 8: Having a history of STDs increases risk
    if std == 'Yes':
        risk += 1
        if num_std_diagnoses > 1:
            risk += 1
        if time_since_first_std < 5:
            risk += 1
        if time_since_last_std < 5:
            risk += 1
    
    return risk

# Define the Streamlit app
def app():
    # Set the title of the web app
    st.title('Cervical Cancer Risk Calculator')
    
    # Create input fields for each variable
    age = st.number_input('Age', min_value=18, max_value=84, value=25)
    num_sexual_partners = st.number_input('Number of Sexual Partners', min_value=0, value=1)
    first_sexual_intercourse = st.number_input('Age at First Sexual Intercourse', min_value=10, max_value=32, value=16)
    num_pregnancies = st.number_input('Number of Pregnancies', min_value=0, value=1)
    smoking = st.selectbox('Do you smoke?', ['Yes', 'No'])
    if smoking == 'Yes':
        smoking_years = st.number_input('How many years have you been smoking?', min_value=0, value=1)
    else:
        smoking_years = 0
    hormonal_contraceptives = st.selectbox('Do you use hormonal contraceptives?', ['Yes', 'No'])
    if hormonal_contraceptives == 'Yes':
        hormonal_contraceptives_years = st.number_input('How many years have you been using hormonal contraceptives?', min_value=0, value=1)
    else:
        hormonal_contraceptives_years = 0
    iud = st.selectbox('Do you use an intrauterine device (IUD)?', ['Yes', 'No'])
    if iud == 'Yes':
        iud_years = st.number_input('How many years have you been using an IUD?', min_value=0, value=1)
    else:
        iud_years = 0
    std = st.selectbox('Have you been diagnosed with a sexually transmitted disease (STD)?', ['Yes', 'No'])
    if std == 'Yes':
        num_std_diagnoses = st.number_input('How many STD diagnoses have you had?', min_value=0, value=1)
        time_since_first_std = st.number_input('How many years ago was your first STD diagnosis?', min_value=0, value=1)
        time_since_last_std = st.number_input('How many years ago was your last STD diagnosis?', min_value=0, value=1)
    else:
        num_std_diagnoses = 0
        time_since_first_std = 0
        time_since_last_std = 0
    
    # Check if the input values meet the rules
    error_message = ''
    for variable, value in zip(['age', 'num_sexual_partners', 'first_sexual_intercourse', 'num_pregnancies', 'smoke', 'smoking_years', 'hormonal_contraceptives', 'hormonal_contraceptives_years', 'iud', 'iud_years', 'stds', 'num_stds', 'time_since_first_std', 'time_since_last_std'], [age, num_sexual_partners, first_sexual_intercourse, num_pregnancies, smoking, smoking_years, hormonal_contraceptives, hormonal_contraceptives_years, iud, iud_years, std, num_std_diagnoses, time_since_first_std, time_since_last_std]):
        if not rules[variable]['rule'](value):
            error_message += rules[variable]['error_message'] + '\n'
    
    # If there is an error, display the error message
    if error_message:
        st.error(error_message)
    else:
        # Calculate the risk of cervical cancer based on the input values
        risk = cervical_cancer_rules(age, num_sexual_partners, first_sexual_intercourse,num_pregnancies,smoke, smoking_years, hormonal_contraceptives, hormonal_contraceptives_years, iud, iud_years, stds, num_stds, time_since_first_std, time_since_last_std)
        # Display the risk of cervical cancer to the user
        st.write(f"Based on the input values, the calculated risk of cervical cancer is {risk}.")

        # Determine the risk category based on the calculated risk
        if risk <= 2:
            category = 'Low'
        elif risk <= 4:
            category = 'Moderate'
        else:
            category = 'High'

        # Display the risk category to the user
        st.write(f"The calculated risk falls into the {category} category.")
