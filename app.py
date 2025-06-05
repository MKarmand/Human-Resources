import streamlit as st
import pandas as pd
import joblib

# Load model dan encoder
model = joblib.load("model.pkl")
label_encoders = joblib.load("encoder.pkl")

st.title("🚨 Employee Attrition Prediction App")

# Input pengguna
st.header("Isi Data Karyawan")
employee_input = {}

employee_input["Age"] = st.slider("Age", 18, 60)
employee_input["BusinessTravel"] = st.selectbox("Business Travel", ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
employee_input["DailyRate"] = st.number_input("Daily Rate", 100, 1500)
employee_input["Department"] = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
employee_input["DistanceFromHome"] = st.slider("Distance From Home (km)", 1, 50)
employee_input["Education"] = st.selectbox("Education Level", [1, 2, 3, 4, 5])
employee_input["EducationField"] = st.selectbox("Education Field", ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other', 'Human Resources'])
employee_input["EnvironmentSatisfaction"] = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
employee_input["Gender"] = st.selectbox("Gender", ["Male", "Female"])
employee_input["HourlyRate"] = st.number_input("Hourly Rate", 10, 100)
employee_input["JobInvolvement"] = st.selectbox("Job Involvement", [1, 2, 3, 4])
employee_input["JobLevel"] = st.selectbox("Job Level", [1, 2, 3, 4, 5])
employee_input["JobRole"] = st.selectbox("Job Role", ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
                                                      'Manufacturing Director', 'Healthcare Representative',
                                                      'Manager', 'Sales Representative', 'Research Director', 'Human Resources'])
employee_input["JobSatisfaction"] = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
employee_input["MaritalStatus"] = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
employee_input["MonthlyIncome"] = st.number_input("Monthly Income", 1000, 20000)
employee_input["MonthlyRate"] = st.number_input("Monthly Rate", 1000, 30000)
employee_input["NumCompaniesWorked"] = st.slider("Num Companies Worked", 0, 10)
employee_input["OverTime"] = st.selectbox("OverTime", ["Yes", "No"])
employee_input["PercentSalaryHike"] = st.slider("Percent Salary Hike", 5, 25)
employee_input["PerformanceRating"] = st.selectbox("Performance Rating", [1, 2, 3, 4])
employee_input["RelationshipSatisfaction"] = st.selectbox("Relationship Satisfaction", [1, 2, 3, 4])
employee_input["StockOptionLevel"] = st.selectbox("Stock Option Level", [0, 1, 2, 3])
employee_input["TotalWorkingYears"] = st.slider("Total Working Years", 0, 40)
employee_input["TrainingTimesLastYear"] = st.slider("Training Times Last Year", 0, 10)
employee_input["WorkLifeBalance"] = st.selectbox("Work Life Balance", [1, 2, 3, 4])
employee_input["YearsAtCompany"] = st.slider("Years At Company", 0, 40)
employee_input["YearsInCurrentRole"] = st.slider("Years In Current Role", 0, 20)
employee_input["YearsSinceLastPromotion"] = st.slider("Years Since Last Promotion", 0, 15)
employee_input["YearsWithCurrManager"] = st.slider("Years With Current Manager", 0, 20)

# Convert to DataFrame
input_df = pd.DataFrame([employee_input])

# Encode kolom kategorikal
for col in input_df.select_dtypes(include='object').columns:
    if col in label_encoders:
        input_df[col] = label_encoders[col].transform(input_df[col])

# Prediksi
if st.button("Prediksi Attrition"):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][1]
    st.subheader("Hasil Prediksi:")
    st.write(f"⚠️ **Attrition:** {'Yes' if prediction == 1 else 'No'}")
    st.write(f"📊 Probabilitas Attrition: {proba:.2%}")
