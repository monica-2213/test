import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
url = 'https://datahub.io/machine-learning/cervical-cancer/r/cervical-cancer.csv'
data = pd.read_csv(url)
# Impute missing values with the median value for each feature
data = data.fillna(data.median())

# Split dataset into features and target
X = data.drop(['Biopsy'], axis=1)
y = data['Biopsy']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest classifier
rfc = RandomForestClassifier(n_estimators=100, random_state=42)
rfc.fit(X_train, y_train)

# Evaluate model on testing set
y_pred = rfc.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Create Streamlit app
st.title("Cervical Cancer Diagnosis Expert System")
st.write("This system predicts the likelihood of cervical cancer based on patient characteristics.")

# Create form for user input
age = st.slider("Age", 14, 84, 25)
number_of_sexual_partners = st.slider("Number of Sexual Partners", 0, 28, 1)
first_sexual_intercourse = st.slider("Age of First Sexual Intercourse", 10, 40, 16)
num_pregnancies = st.slider("Number of Pregnancies", 0, 11, 0)
smokes = st.selectbox("Smoking Status", ["Never", "Former", "Current"])
smokes_years = st.slider("Years of Smoking", 0, 50, 0)
smokes_packs = st.slider("Packs of Smoking per Year", 0, 100, 0)
hormonal_contraceptives = st.selectbox("Hormonal Contraceptives", ["Yes", "No"])
iud = st.selectbox("IUD", ["Yes", "No"])
stds = st.selectbox("STDs", ["Yes", "No"])
stds_number = st.slider("Number of STDs", 0, 7, 0)
stds_condylomatosis = st.selectbox("Condylomatosis", ["Yes", "No"])
stds_cervical_condylomatosis = st.selectbox("Cervical Condylomatosis", ["Yes", "No"])
stds_vaginal_condylomatosis = st.selectbox("Vaginal Condylomatosis", ["Yes", "No"])
stds_vulvo_perineal_condylomatosis = st.selectbox("Vulvo-perineal Condylomatosis", ["Yes", "No"])
stds_syphilis = st.selectbox("Syphilis", ["Yes", "No"])
stds_pelvic_inflammatory_disease = st.selectbox("Pelvic Inflammatory Disease", ["Yes", "No"])
stds_genital_herpes = st.selectbox("Genital Herpes", ["Yes", "No"])
stds_molluscum_contagiosum = st.selectbox("Molluscum Contagiosum", ["Yes", "No"])
stds_aids = st.selectbox("AIDS", ["Yes", "No"])
stds_hiv = st.selectbox("HIV", ["Yes", "No"])
stds_hepatitis_b = st.selectbox("Hepatitis B", ["Yes", "No"])

# Create prediction button
if st.button("Predict"):
    # Create input data
    input_data = {
        'Age': age,
        'Number of sexual partners': number_of_sexual_partners,
        'First sexual intercourse': first_sexual_intercourse,
        'Num of pregnancies': num_pregnancies,
        'Smokes': 1 if smokes == "Former" or smokes == "Current" else 0,
        'Smokes (years)': smokes_years,
        'Smokes (packs/year)': smokes_packs,
        'Hormonal Contraceptives': 1 if hormonal_contraceptives == "Yes" else 0,
        'IUD': 1 if iud == "Yes" else 0,
        'STDs': 1 if stds == "Yes" else 0,
        'STDs (number)': stds_number,
        'STDs:condylomatosis': 1 if stds_condylomatosis == "Yes" else 0,
        'STDs:cervical condylomatosis': 1 if stds_cervical_condylomatosis == "Yes" else 0,
        'STDs:vaginal condylomatosis': 1 if stds_vaginal_condylomatosis == "Yes" else 0,
        'STDs:vulvo-perineal condylomatosis': 1 if stds_vulvo_perineal_condylomatosis == "Yes" else 0,
        'STDs:syphilis': 1 if stds_syphilis == "Yes" else 0,
        'STDs:pelvic inflammatory disease': 1 if stds_pelvic_inflammatory_disease == "Yes" else 0,
        'STDs:genital herpes': 1 if stds_genital_herpes == "Yes" else 0,
        'STDs:molluscum contagiosum': 1 if stds_molluscum_contagiosum == "Yes" else 0,
        'STDs:AIDS': 1 if stds_aids == "Yes" else 0,
        'STDs:HIV': 1 if stds_hiv == "Yes" else 0,
        'STDs:hepatitis B': 1 if stds_hepatitis_b == "Yes" else 0
    }

    # Predict on input data
    pred = rfc.predict(pd.DataFrame([input_data]))

    # Map prediction to diagnosis
    diagnosis = "Positive" if pred[0] == 1 else "Negative"

    # Display diagnosis
    st.write(f"Based on the input data, the diagnosis is {diagnosis}.")

