import streamlit as st
import pandas as pd
from student_details import Student

st.set_page_config(page_title="Student Management", page_icon="🎓", layout="centered")

st.title("🎓 Student Management System")

# Session state to store students across interactions
if "students" not in st.session_state:
    st.session_state.students = []

# Sidebar - Add student form
st.sidebar.header("➕ Add Student")
name = st.sidebar.text_input("Enter Student Name:")
roll_no = st.sidebar.number_input("Enter Roll Number:", min_value=1, step=1)
marks = st.sidebar.number_input("Enter Marks:", min_value=0, max_value=100, step=1)

if st.sidebar.button("Add Student"):
    new_student = Student(name, roll_no, marks)
    st.session_state.students.append(new_student.student_det())
    st.sidebar.success(f"✅ {name} added successfully!")

# Show all students in a table
st.subheader("📋 All Students")
if st.session_state.students:
    df = pd.DataFrame(st.session_state.students)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No students added yet.")

# Search student by roll number
st.subheader("🔍 Search Student by Roll Number")
search_roll = st.number_input("Enter Roll Number to search:", min_value=1, step=1)
if st.button("Search"):
    result = [s for s in st.session_state.students if s["Roll Number"] == search_roll]
    if result:
        st.success("✅ Student Found!")
        st.table(result)
    else:
        st.error("❌ No student found with that Roll Number.")

# Clear all students
if st.button("🗑️ Clear All Students"):
    st.session_state.students = []
    st.warning("All student records have been cleared.")
