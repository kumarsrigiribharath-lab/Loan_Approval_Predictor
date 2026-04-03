import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Loan Predictor", layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0e1117;
    color: white;
}
/* Labels (THIS IS YOUR FIX) */
label {
    color: white !important;
    font-weight: 500;
}
/* Section headers */
h1, h2, h3, h4, h5, h6 {
    color: white !important;
}
/* Selectbox text */
div[data-baseweb="select"] {
    color: black;
}
/* Input box text */
input {
    color: black !important;
}
.stButton>button {
    background-color: #00adb5;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>💰 Loan Approval Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Enter applicant details to predict loan approval</p>", unsafe_allow_html=True)

st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Personal Details:")

    gender = st.selectbox("Gender", ["Select", "Male", "Female"])
    married = st.selectbox("Married", ["Select", "Yes", "No"])
    dependents = st.selectbox("Dependents", ["Select", "0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Select", "Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Select", "Yes", "No"])

with col2:
    st.subheader("💼 Financial Details:")

    applicant_income = st.text_input("Applicant Income", placeholder="e.g., 5000")
    coapplicant_income = st.text_input("Coapplicant Income", placeholder="e.g., 2000")
    loan_amount = st.text_input("Loan Amount", placeholder="e.g., 150")
    loan_term = st.text_input("Loan Term", placeholder="e.g., 360")

    credit_history = st.selectbox("Credit History", ["Select", 1, 0])
    property_area = st.selectbox("Property Area", ["Select", "Urban", "Semiurban", "Rural"])

if st.button("🚀 Predict Loan Status"):
    if (
        "Select" in [gender, married, dependents, education, self_employed, credit_history, property_area]
        or applicant_income == ""
        or loan_amount == ""
        or loan_term == ""
    ):
        st.warning("⚠️ Please fill all fields correctly")

    else:
        try:
            applicant_income = float(applicant_income)
            coapplicant_income = float(coapplicant_income) if coapplicant_income != "" else 0
            loan_amount = float(loan_amount)
            loan_term = float(loan_term)
        except:
            st.error("⚠️ Please enter valid numeric values!")
            st.stop()

        dependents = 3 if dependents == "3+" else int(dependents)

        gender = 1 if gender == "Male" else 0
        married = 1 if married == "Yes" else 0
        education = 1 if education == "Graduate" else 0
        self_employed = 1 if self_employed == "Yes" else 0

        property_map = {"Rural": 0, "Semiurban": 1, "Urban": 2}
        property_area = property_map[property_area]

        input_data = pd.DataFrame([[
            gender, married, dependents, education, self_employed,
            applicant_income, coapplicant_income, loan_amount,
            loan_term, credit_history, property_area
        ]], columns=[
            "Gender","Married","Dependents","Education","Self_Employed",
            "ApplicantIncome","CoapplicantIncome","LoanAmount",
            "Loan_Amount_Term","Credit_History","Property_Area"
        ])

        input_data = scaler.transform(input_data)
        prediction = model.predict(input_data)[0]

        try:
            prob = model.predict_proba(input_data)[0][1]
        except:
            prob = None

        st.divider()
        st.subheader("📊 Predicted Result")

        if prediction == 1:
            st.markdown(f"""
                <div style="
                    background-color:#0f5132;
                    padding:25px;
                    border-radius:12px;
                    text-align:center;
                    font-size:24px;
                    font-weight:bold;
                    color:#d1e7dd;
                    border:2px solid #198754;">
                    ✅ Loan Approved...
                    <br><br>
                    {"Approval Probability: " + format(prob, ".2f") if prob is not None else ""}
                </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown(f"""
                <div style="
                    background-color:#842029;
                    padding:25px;
                    border-radius:12px;
                    text-align:center;
                    font-size:24px;
                    font-weight:bold;
                    color:#f8d7da;
                    border:2px solid #dc3545;">
                    ❌ Loan Not Approved...
                    <br><br>
                    {"Approval Probability: " + format(prob, ".2f") if prob is not None else ""}
                </div>
            """, unsafe_allow_html=True)
