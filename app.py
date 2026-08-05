
import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("promotion_model.pkl")

st.set_page_config(
    page_title="Employee Promotion Prediction",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Employee Promotion Prediction System")
st.markdown("---")

st.header("Employee Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 65, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    education = st.selectbox(
        "Education Level",
        ["High School", "Diploma", "Bachelor", "Master", "PhD"]
    )
    marital = st.selectbox(
        "Marital Status",
        ["Single", "Married", "Divorced"]
    )
    city_tier = st.selectbox("City Tier", [1, 2, 3])

with col2:
    department = st.selectbox(
        "Department",
        ["HR", "Sales", "IT", "Finance", "Marketing", "Operations"]
    )
    employment_type = st.selectbox(
        "Employment Type",
        ["Permanent", "Contract", "Intern"]
    )
    years_company = st.number_input("Years at Company", 0, 40, 5)
    current_role = st.number_input("Years in Current Role", 0, 20, 2)
    last_promotion = st.number_input("Years Since Last Promotion", 0, 15, 1)

st.markdown("---")

st.header("Performance Details")

team_size = st.number_input("Team Size", 1, 100, 10)

performance_score = st.slider("Performance Score", 0.0, 10.0, 7.5)
performance_last = st.slider("Performance Last Year", 0.0, 10.0, 7.0)
performance_two = st.slider("Performance Two Years Ago", 0.0, 10.0, 6.5)

manager_rating = st.slider("Manager Rating", 1.0, 5.0, 4.0)
peer_feedback = st.slider("Peer Feedback Score", 0.0, 10.0, 8.0)

projects = st.number_input("Projects Completed", 0, 100, 10)

kpi = st.slider("KPI Achievement (%)", 0, 100, 80)

innovation = st.slider("Innovation Score", 0.0, 10.0, 7.0)

leadership = st.slider("Leadership Score", 0.0, 10.0, 7.0)

problem = st.slider("Problem Solving Score", 0.0, 10.0, 7.0)

st.markdown("---")

st.header("Work Information")

avg_hours = st.number_input("Average Monthly Hours", 50, 350, 170)
overtime = st.number_input("Overtime Hours", 0, 100, 10)
tasks = st.number_input("Tasks Completed", 0, 500, 100)
deadline = st.slider("Deadline Adherence Rate (%)", 0, 100, 90)
meeting = st.number_input("Meeting Hours Per Month", 0, 100, 15)
remote = st.slider("Remote Work Ratio (%)", 0, 100, 20)

st.markdown("---")

st.header("Training & Salary")

training = st.number_input("Training Hours Last Year", 0, 500, 40)
certifications = st.number_input("Certifications Count", 0, 20, 2)
skill = st.slider("Skill Assessment Score", 0, 100, 75)

cross_projects = st.number_input("Cross Department Projects", 0, 20, 2)
mentoring = st.number_input("Mentoring Sessions", 0, 50, 5)

salary = st.number_input("Salary", 10000, 1000000, 50000)
salary_increase = st.slider("Salary Increase (%)", 0.0, 50.0, 10.0)

bonus = st.number_input("Bonus Last Year", 0, 500000, 50000)
stock = st.number_input("Stock Options", 0, 10000, 100)

attendance = st.slider("Attendance Rate (%)", 0.0, 100.0, 95.0)
late_days = st.number_input("Late Days", 0, 365, 5)

engagement = st.slider("Employee Engagement Score", 0.0, 10.0, 8.0)
job = st.slider("Job Satisfaction Score", 0.0, 10.0, 8.0)
mobility = st.slider("Internal Mobility Score", 0.0, 10.0, 7.0)

if st.button("Predict Promotion"):

    gender = 1 if gender == "Male" else 0

    education = {
        "High School": 0,
        "Diploma": 1,
        "Bachelor": 2,
        "Master": 3,
        "PhD": 4
    }[education]

    marital = {
        "Single": 0,
        "Married": 1,
        "Divorced": 2
    }[marital]

    department = {
        "HR": 0,
        "Sales": 1,
        "IT": 2,
        "Finance": 3,
        "Marketing": 4,
        "Operations": 5
    }[department]

    employment_type = {
        "Permanent": 0,
        "Contract": 1,
        "Intern": 2
    }[employment_type]

    input_data = pd.DataFrame([[
        age,
        gender,
        education,
        marital,
        city_tier,
        department,
        employment_type,
        years_company,
        current_role,
        last_promotion,
        team_size,
        performance_score,
        performance_last,
        performance_two,
        manager_rating,
        peer_feedback,
        projects,
        kpi,
        innovation,
        leadership,
        problem,
        avg_hours,
        overtime,
        tasks,
        deadline,
        meeting,
        remote,
        training,
        certifications,
        skill,
        cross_projects,
        mentoring,
        salary,
        salary_increase,
        bonus,
        stock,
        attendance,
        late_days,
        engagement,
        job,
        mobility
    ]])

    prediction = model.predict(input_data)

    st.markdown("---")

    if prediction[0] == 1:
        st.success("🎉 Congratulations! Employee is likely to be PROMOTED.")
        st.balloons()
    else:

import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("promotion_model.pkl")

st.set_page_config(
    page_title="Employee Promotion Prediction",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Employee Promotion Prediction System")
st.markdown("---")

st.header("Employee Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 65, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    education = st.selectbox(
        "Education Level",
        ["High School", "Diploma", "Bachelor", "Master", "PhD"]
    )
    marital = st.selectbox(
        "Marital Status",
        ["Single", "Married", "Divorced"]
    )
    city_tier = st.selectbox("City Tier", [1, 2, 3])

with col2:
    department = st.selectbox(
        "Department",
        ["HR", "Sales", "IT", "Finance", "Marketing", "Operations"]
    )
    employment_type = st.selectbox(
        "Employment Type",
        ["Permanent", "Contract", "Intern"]
    )
    years_company = st.number_input("Years at Company", 0, 40, 5)
    current_role = st.number_input("Years in Current Role", 0, 20, 2)
    last_promotion = st.number_input("Years Since Last Promotion", 0, 15, 1)

st.markdown("---")

st.header("Performance Details")

team_size = st.number_input("Team Size", 1, 100, 10)

performance_score = st.slider("Performance Score", 0.0, 10.0, 7.5)
performance_last = st.slider("Performance Last Year", 0.0, 10.0, 7.0)
performance_two = st.slider("Performance Two Years Ago", 0.0, 10.0, 6.5)

manager_rating = st.slider("Manager Rating", 1.0, 5.0, 4.0)
peer_feedback = st.slider("Peer Feedback Score", 0.0, 10.0, 8.0)

projects = st.number_input("Projects Completed", 0, 100, 10)

kpi = st.slider("KPI Achievement (%)", 0, 100, 80)

innovation = st.slider("Innovation Score", 0.0, 10.0, 7.0)

leadership = st.slider("Leadership Score", 0.0, 10.0, 7.0)

problem = st.slider("Problem Solving Score", 0.0, 10.0, 7.0)

st.markdown("---")

st.header("Work Information")

avg_hours = st.number_input("Average Monthly Hours", 50, 350, 170)
overtime = st.number_input("Overtime Hours", 0, 100, 10)
tasks = st.number_input("Tasks Completed", 0, 500, 100)
deadline = st.slider("Deadline Adherence Rate (%)", 0, 100, 90)
meeting = st.number_input("Meeting Hours Per Month", 0, 100, 15)
remote = st.slider("Remote Work Ratio (%)", 0, 100, 20)

st.markdown("---")

st.header("Training & Salary")

training = st.number_input("Training Hours Last Year", 0, 500, 40)
certifications = st.number_input("Certifications Count", 0, 20, 2)
skill = st.slider("Skill Assessment Score", 0, 100, 75)

cross_projects = st.number_input("Cross Department Projects", 0, 20, 2)
mentoring = st.number_input("Mentoring Sessions", 0, 50, 5)

salary = st.number_input("Salary", 10000, 1000000, 50000)
salary_increase = st.slider("Salary Increase (%)", 0.0, 50.0, 10.0)

bonus = st.number_input("Bonus Last Year", 0, 500000, 50000)
stock = st.number_input("Stock Options", 0, 10000, 100)

attendance = st.slider("Attendance Rate (%)", 0.0, 100.0, 95.0)
late_days = st.number_input("Late Days", 0, 365, 5)

engagement = st.slider("Employee Engagement Score", 0.0, 10.0, 8.0)
job = st.slider("Job Satisfaction Score", 0.0, 10.0, 8.0)
mobility = st.slider("Internal Mobility Score", 0.0, 10.0, 7.0)

if st.button("Predict Promotion"):

    gender = 1 if gender == "Male" else 0

    education = {
        "High School": 0,
        "Diploma": 1,
        "Bachelor": 2,
        "Master": 3,
        "PhD": 4
    }[education]

    marital = {
        "Single": 0,
        "Married": 1,
        "Divorced": 2
    }[marital]

    department = {
        "HR": 0,
        "Sales": 1,
        "IT": 2,
        "Finance": 3,
        "Marketing": 4,
        "Operations": 5
    }[department]

    employment_type = {
        "Permanent": 0,
        "Contract": 1,
        "Intern": 2
    }[employment_type]

    input_data = pd.DataFrame([[
        age,
        gender,
        education,
        marital,
        city_tier,
        department,
        employment_type,
        years_company,
        current_role,
        last_promotion,
        team_size,
        performance_score,
        performance_last,
        performance_two,
        manager_rating,
        peer_feedback,
        projects,
        kpi,
        innovation,
        leadership,
        problem,
        avg_hours,
        overtime,
        tasks,
        deadline,
        meeting,
        remote,
        training,
        certifications,
        skill,
        cross_projects,
        mentoring,
        salary,
        salary_increase,
        bonus,
        stock,
        attendance,
        late_days,
        engagement,
        job,
        mobility
    ]])

    prediction = model.predict(input_data)

    st.markdown("---")

    if prediction[0] == 1:
        st.success("🎉 Congratulations! Employee is likely to be PROMOTED.")
        st.balloons()
    else:

        st.error("❌ Employee is NOT likely to be promoted.")