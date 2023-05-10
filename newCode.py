import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
url = "https://datahub.io/machine-learning/cervical-cancer/r/cervical-cancer.csv"
df = pd.read_csv(url)

# Preprocess the data
df = df.replace('?', np.nan)
df = df.dropna()

# Split the data into training and testing sets
X = df.drop('Biopsy', axis=1)
y = df['Biopsy']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Define the expert system
def expert_system(age, number_of_sexual_partners, first_sexual_intercourse, num_pregnancies, smokes, smokes_years, smokes_packs_year, hormonal_contraceptives, hormonal_contraceptives_years, iud, iud_years, stds, stds_number):
    input_data = np.array([age, number_of_sexual_partners, first_sexual_intercourse, num_pregnancies, smokes, smokes_years, smokes_packs_year, hormonal_contraceptives, hormonal_contraceptives_years, iud, iud_years, stds, stds_number]).reshape(1, -1)
    prediction = clf.predict(input_data)
    if prediction[0] == 0:
        return "You are not at risk of cervical cancer."
    else:
        return "You may be at risk of cervical cancer. Please consult a doctor."

# Define the Streamlit app
st.title("Cervical Cancer Expert System")

age = st.number_input("What is your age?", min_value=1, max_value=100, value=25)
number_of_sexual_partners = st.number_input("How many sexual partners have you had?", min_value=0, value=0)
first_sexual_intercourse = st.number_input("What was your age at first sexual intercourse?", min_value=1, max_value=100, value=18)
num_pregnancies = st.number_input("How many times have you been pregnant?", min_value=0, value=0)
smokes = st.selectbox("Do you smoke?", ("Yes", "No"))
if smokes == "Yes":
    smokes_years = st.number_input("For how many years have you been smoking?", min_value=1, value=1)
    smokes_packs_year = st.number_input("How many packs of cigarettes do you smoke per year?", min_value=1, value=1)
else:
    smokes_years = 0
    smokes_packs_year = 0
hormonal_contraceptives = st.selectbox("Have you ever used hormonal contraceptives?", ("Yes", "No"))
if hormonal_contraceptives == "Yes":
    hormonal_contraceptives_years = st.number_input("For how many years have you used hormonal contraceptives?", min_value=1, value=1)
else:
    hormonal_contraceptives_years = 0
iud = st.selectbox("Have you ever used an intrauterine device (IUD)?", ("Yes", "No"))
if iud == "Yes":
    iud_years = st.number_input("For how many years have you used an IUD?", min_value=1, value=1)
else:
    iud_years = 0
stds = st.selectbox("Have you ever had a sexually transmitted disease?", ("Yes", "No"))
if stds == "Yes":
    stds_number = st.number_input("How many sexually transmitted diseases have you had?", min_value=1, value=1)
else:
    stds_number = 0

if st.button("Submit"):
    # Convert binary categorical variables to numerical
    X_test["Smokes"] = X_test["Smokes"].map({"yes": 1, "no": 0})
    X_test["Hormonal Contraceptives"] = X_test["Hormonal Contraceptives"].map({"yes": 1, "no": 0})
    X_test["IUD"] = X_test["IUD"].map({"yes": 1, "no": 0})
    X_test["STDs"] = X_test["STDs"].map({"yes": 1, "no": 0})

    # Convert input data to numerical values
    smokes_num = 1 if smokes == "Yes" else 0
    hormonal_contraceptives_num = 1 if hormonal_contraceptives == "Yes" else 0
    iud_num = 1 if iud == "Yes" else 0
    stds_num = 1 if stds == "Yes" else 0

    # Create input data array
    input_data = np.array([age, number_of_sexual_partners, first_sexual_intercourse, num_pregnancies, smokes_num, smokes_years, smokes_packs_year, hormonal_contraceptives_num, hormonal_contraceptives_years, iud_num, iud_years, stds_num, stds_number]).reshape(1, -1)

    # Make prediction
    prediction = clf.predict(input_data)

    # Show result
    if prediction[0] == 0:
        st.write("You are not at risk of cervical cancer.")
    else:
        st.write("You may be at risk of cervical cancer. Please consult a doctor.")
