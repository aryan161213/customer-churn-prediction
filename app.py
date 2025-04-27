import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('best_random_forest_churn.pkl')

st.title('Customer Churn Prediction')

# Input fields
gender = st.text_input('Gender (0 for Female, 1 for Male)')
SeniorCitizen = st.text_input('Senior Citizen (0 or 1)')
Partner = st.text_input('Partner (0 or 1)')
Dependents = st.text_input('Dependents (0 or 1)')
tenure = st.text_input('Tenure (number of months)')
PhoneService = st.text_input('Phone Service (0 or 1)')
MultipleLines = st.text_input('Multiple Lines (0 or 1)')
InternetService = st.text_input('Internet Service (0: DSL, 1: Fiber optic, 2: No)')
OnlineSecurity = st.text_input('Online Security (0 or 1)')
OnlineBackup = st.text_input('Online Backup (0 or 1)')
DeviceProtection = st.text_input('Device Protection (0 or 1)')
TechSupport = st.text_input('Tech Support (0 or 1)')
StreamingTV = st.text_input('Streaming TV (0 or 1)')
StreamingMovies = st.text_input('Streaming Movies (0 or 1)')
Contract = st.text_input('Contract (0: Month-to-month, 1: One year, 2: Two year)')
PaperlessBilling = st.text_input('Paperless Billing (0 or 1)')
PaymentMethod = st.text_input('Payment Method (0, 1, 2, or 3)')
MonthlyCharges = st.text_input('Monthly Charges (float)')
TotalCharges = st.text_input('Total Charges (float)')

# Predict button
if st.button('Predict Churn'):
    try:
        # Collect inputs
        input_data = np.array([
            float(gender), float(SeniorCitizen), float(Partner), float(Dependents),
            float(tenure), float(PhoneService), float(MultipleLines), float(InternetService),
            float(OnlineSecurity), float(OnlineBackup), float(DeviceProtection),
            float(TechSupport), float(StreamingTV), float(StreamingMovies), float(Contract),
            float(PaperlessBilling), float(PaymentMethod), float(MonthlyCharges),
            float(TotalCharges)
        ]).reshape(1, -1)

        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error('⚠️ The customer is likely to churn!')
        else:
            st.success('✅ The customer is likely to stay!')
    except:
        st.warning('Please fill all fields correctly!')
