# LOAN APPROVAL PREDICTOR:

# Overview:

An end-to-end Machine Learning application that predicts loan approval status based on applicant financial and personal details.
This project simulates a real-world banking scenario where financial institutions assess loan eligibility using data-driven decision-making.

# Key Features:

* Predicts loan approval (Approved / Not Approved)
* Displays **approval probability (confidence score)**
* Clean, responsive **Streamlit web interface**
* Input validation for robust user experience

# Machine Learning Models:

The following models were trained and evaluated:
* Logistic Regression
* Random Forest Classifier
* Support Vector Machine (SVM)

**Best Model Selected:** Random Forest Classifier
(based on highest accuracy and stable performance)

# Tech Stack:

* Python 
* Pandas & NumPy (Data Processing)
* Scikit-learn (Model Building)
* Streamlit (Web App Deployment)

# Model Performance:

* Logistic Regression     =88%     
* Random Forest           =90%         
* SVM                     =89%      

> Random Forest outperformed other models with better generalization.

# Project Structure:

Loan-Approval-Predictor:

    loan_dataset.csv->model(model.pkl)->train.py->app.py->requirements.txt->README.md

# How It Works:

1. User enters applicant details
2. Data is preprocessed & encoded
3. Model predicts loan status
4. Probability score is displayed

# Output:

* Loan Approval Status
* Probability Score

# Project Preview:
# Loan Approved Predictor:
<img width="1900" height="835" alt="IP_data" src="https://github.com/user-attachments/assets/1d14ef80-bc57-4879-9f23-cd6d52819c4c" />
<img width="1897" height="816" alt="OP_approved" src="https://github.com/user-attachments/assets/c09e010f-20f8-48a2-8699-fd719a51919f" />

# Loan Unapproved Predictor:
<img width="1872" height="807" alt="IP_unapproved" src="https://github.com/user-attachments/assets/0f0e4c81-a50f-4106-b5f6-ef641eef15d8" />
<img width="1910" height="830" alt="OP_unapproved" src="https://github.com/user-attachments/assets/ea59878b-a2a5-41e5-9254-000576639cc5" />

# Live DEMO:

https://loanapprovalpredictor-suoxewdw2r9vhem73sg9ug.streamlit.app/

# Key Learnings:

* Data preprocessing & missing value handling
* Feature encoding techniques
* Model selection & evaluation
* Deploying ML models with Streamlit

# Future Enhancements:

* Feature importance visualization
* Hyperparameter tuning
* Cloud deployment (Streamlit / AWS)
* Add explainability (SHAP / LIME)

# Author:

Srigiribharath K
Aspiring Machine Learning Engineer
