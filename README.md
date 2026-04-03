# Loan Approval Predictor:

# Overview:

An end-to-end Machine Learning web application that predicts loan approval status based on applicant financial and personal details.
This project simulates a real-world banking scenario where institutions assess loan eligibility using data-driven decision-making.

# Live Demo:

https://loanapprovalpredictor-suoxewdw2r9vhem73sg9ug.streamlit.app/

# Key Features:

* Predicts loan approval (Approved / Not Approved)
* Displays approval probability (confidence score)
* Clean and responsive Streamlit interface
* Input validation for improved user experience

# Machine Learning Models:

The following models were trained and evaluated:

* Logistic Regression
* Random Forest Classifier
* Support Vector Machine (SVM)

# Model Performance:

# Model & Accuracy:
* Logistic Regression => 88%
* Random Forest => 90%
* SVM => 89%

Random Forest outperformed other models with better generalization.

# Tech Stack:

* Python
* Pandas and NumPy
* Scikit-learn
* Streamlit

# How It Works:

1. User enters applicant details
2. Data is preprocessed and encoded
3. Model predicts loan status
4. Probability score is displayed

# Prediction Results:

# Loan Approved Case:

<img width="1900" height="835" alt="IP_data" src="https://github.com/user-attachments/assets/1d14ef80-bc57-4879-9f23-cd6d52819c4c" />
<img width="1897" height="816" alt="OP_approved" src="https://github.com/user-attachments/assets/c09e010f-20f8-48a2-8699-fd719a51919f" />

# Loan Not Approved Case:

<img width="1872" height="807" alt="IP_unapproved" src="https://github.com/user-attachments/assets/0f0e4c81-a50f-4106-b5f6-ef641eef15d8" />
<img width="1910" height="830" alt="OP_unapproved" src="https://github.com/user-attachments/assets/ea59878b-a2a5-41e5-9254-000576639cc5" />

# Project Structure:

Loan-Approval-Predictor/
1.app.py
2.train.py
3.requirements.txt
4.README.md
   * model/
     a)model.pkl
     b)scaler.pkl
   * data/
     a)loan_dataset.csv
   * images/
     a)approved.png
     b)not_approved.png

# How to Run Locally:

* git clone https://github.com/kumarsrigiribharath-lab/Loan_Approval_Predictor/tree/main
* cd Loan_Approval_Predictor
* pip install -r requirements.txt
* python train.py
* streamlit run app.py

# Key Learnings:

* Data preprocessing and missing value handling
* Feature encoding techniques
* Model selection and evaluation
* Handling imbalanced datasets using SMOTE
* Deploying Machine Learning applications using Streamlit

# Future Enhancements:

* Integrate deep learning models (CNN) for advanced prediction tasks
* Extend the application to medical diagnosis use-cases
* Implement explainable AI techniques (SHAP / LIME)
* Perform hyperparameter tuning
* Deploy scalable versions using cloud platforms

# Author:

Srigiribharath K
Aspiring Machine Learning Engineer

# Support:

If you find this project useful, consider giving it a star on GitHub.
