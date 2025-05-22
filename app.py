import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('/Users/mohammedmahmood/Desktop/Data projects/Data science/Telecome_Churn_Prediction /Telecom_churn_prediction.sav', "rb") as file:
    model = pickle.load(file)

st.title(" Telecom Customer Churn Prediction App")
st.markdown("Enter the customer usage details below to predict if they are likely to churn.")

# Input widgets with correct ranges based on your data summary
international_plan = st.selectbox("International Plan", ["No", "Yes"])
voice_mail_plan = st.selectbox("Voice Mail Plan", ["No", "Yes"])

total_day_minutes = st.slider("Total Day Minutes", 0.0, 350.8, 179.8)
total_eve_minutes = st.slider("Total Evening Minutes", 0.0, 363.7, 201.0)
total_night_minutes = st.slider("Total Night Minutes", 23.2, 395.0, 200.9)
# Auto calculate totals
tota_minutes = total_day_minutes + total_eve_minutes + total_night_minutes
st.metric("Total Minutes (Auto Calculated)", f"{tota_minutes:.2f}") 

total_day_charge = st.slider("Total Day Charge", 0.0, 59.64, 30.56)
total_eve_charge = st.slider("Total Evening Charge", 0.0, 30.91, 17.08)
total_night_charge = st.slider("Total Night Charge", 1.04, 17.77, 9.04)
# Auto calculate totals
total_charge = total_day_charge + total_eve_charge + total_night_charge
st.metric("Total Charge (Auto Calculated)", f"{total_charge:.2f}")

total_intl_minutes = st.slider("Total International Minutes", 0.0, 20.0, 10.2)
total_intl_calls = st.slider("Total International Calls", 0, 20, 4)
total_intl_charge = st.slider("Total International Charge", 0.0, 5.4, 2.76)

customer_service_calls = st.slider("Customer Service Calls", 0, 9, 1)


# Prepare DataFrame for prediction
input_data = pd.DataFrame([{
    'International_plan': international_plan,
    'Voice_mail_plan': voice_mail_plan,
    'Total_day_minutes': total_day_minutes,
    'Total_day_charge': total_day_charge,
    'Total_eve_minutes': total_eve_minutes,
    'Total_eve_charge': total_eve_charge,
    'Total_night_minutes': total_night_minutes,
    'Total_night_charge': total_night_charge,
    'Total_intl_minutes': total_intl_minutes,
    'Total_intl_calls': total_intl_calls,
    'Total_intl_charge': total_intl_charge,
    'Customer_service_calls': customer_service_calls,
    'total_charge': total_charge,
    'tota_minutes': tota_minutes
}])

# Prediction button
if st.button("Predict Churn"):
    try:
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.error(" This customer is likely to churn based on his information!")
        else:
            st.success("✅ This customer is likely to staybased on his information!")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
