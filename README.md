# SMART LOAN APPROVAL PREDICTOR:

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

        Model            Accuracy 
  Logistic Regression      88%     
  Random Forest            90% 
  SVM                      89%      

> Random Forest outperformed other models with better generalization.

# Project Structure:

loan-approval-predictor = data, loan_data.csv, model(model.pkl), train.py, app.py, requirements.txt, README.md

# How It Works:

1. User enters applicant details
2. Data is preprocessed & encoded
3. Model predicts loan status
4. Probability score is displayed

# Run Locally:

```bash
git clone https://github.com/YOUR_USERNAME/loan-approval-predictor.git
cd loan-approval-predictor

pip install -r requirements.txt
python train.py
streamlit run app.py
```

# Output:

* Loan Approval Status
* Probability Score (Model Confidence)

# Project Preview:

![input_data](https://github.com/user-attachments/assets/a1f9ae8c-a494-4ed6-959a-9f1516e02b95)
![Approval_output](https://github.com/user-attachments/assets/a5e98180-a6c3-4aca-93af-ff8713da07ce)
  
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
