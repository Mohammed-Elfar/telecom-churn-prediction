import streamlit as st
import pickle
import pandas as pd

# ================= Load Model =================
with open('/Users/mohammedmahmood/Desktop/Data projects/Data science/Telecome_Churn_Prediction /Telecome_Churn_Prediction.sav', "rb") as file:
    model = pickle.load(file)

st.title("📞 Telecom Customer Churn Prediction App")
st.markdown("Enter the customer’s details below to predict if they are likely to churn.")

# ================= Inputs =================
col1, col2 = st.columns(2)

with col1:
    international_plan = st.selectbox("International Plan", ["No", "Yes"])
    voice_mail_plan = st.selectbox("Voice Mail Plan", ["No", "Yes"])
    account_length = st.slider("Account Length", 1, 243, 120)
    number_vmail_messages = st.slider("Number of Voice Mail Messages", 0, 51, 10)

with col2:
    total_day_charge = st.slider("Total Day Charge", 0.0, 59.64, 30.56)
    total_eve_charge = st.slider("Total Evening Charge", 0.0, 30.91, 17.08)
    total_night_charge = st.slider("Total Night Charge", 1.04, 17.77, 9.04)
    total_intl_calls = st.slider("Total International Calls", 0, 20, 4)
    total_intl_charge = st.slider("Total International Charge", 0.0, 5.4, 2.76)

# Auto calculate totals
Total_charge = total_day_charge + total_eve_charge + total_night_charge
st.metric("Total Charge (Auto Calculated)", f"{Total_charge:.2f}")

customer_service_calls = st.slider("Customer Service Calls", 0, 9, 1)

# --- Automatically set High_service_calls ---
if customer_service_calls > 3:
    high_service_calls = 1
else:
    high_service_calls = 0

# Show the calculated result (so user knows)
st.metric("📞 High Service Calls (> 3 customer service calls for user will be in High Service Calls )", f"{high_service_calls}")


# ================= Prepare Input Data =================
input_data = pd.DataFrame([{
    'Account_length': account_length,
    'International_plan': international_plan,
    'Voice_mail_plan': voice_mail_plan,
    'Number_vmail_messages': number_vmail_messages,
    'Total_day_charge': total_day_charge,
    'Total_eve_charge': total_eve_charge,
    'Total_night_charge': total_night_charge,
    'Total_intl_calls': total_intl_calls,
    'Total_intl_charge': total_intl_charge,
    'Customer_service_calls': customer_service_calls,
    'High_service_calls': high_service_calls,
    'Total_charge': Total_charge,
}])

# ================= Prediction =================
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]

    # Predict probability (Random Forest supports this)
    proba = model.predict_proba(input_data)[0][1]  # probability of churn (class = 1)

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"This customer is **likely to CHURN** with (Probability of: {proba:.2%})")
    else:
        st.success(f"This customer is **likely to STAY** with (Probability of churn: {proba:.2%})")
