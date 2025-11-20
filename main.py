import streamlit as st
from postgresql_script import get_connection
import psycopg2

# Page config
st.set_page_config(page_title="Simple Form App", page_icon="📝")

# Title
st.title("📝 Simple Form Application")
st.write("Fill out the forms below to submit your information.")

# Divider
st.divider()

# Form 1: Personal Information
st.header("Personal Information")
with st.form("personal_info"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    
    submitted1 = st.form_submit_button("Submit Personal Info")
    
    if submitted1:
        st.success(f"✅ Personal info submitted for {name}!")
        st.write(f"Email: {email}")
        st.write(f"Age: {age}")

        # Send this information to PostgreSQL
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO personal_info (name, email, age) VALUES (%s, %s, %s) RETURNING id",
                    (name, email, age)
                )
                result = cursor.fetchone()
                conn.commit()
                print(f"Record inserted with ID: {result[0]}")
                cursor.close()
                conn.close()
            except psycopg2.Error as e:
                print(f"Error inserting data: {e}")
                if conn:
                    conn.rollback()
                    conn.close()
        else:
            st.error("Failed to connect to database")

st.divider()

# Form 2: Feedback
st.header("Feedback Form")
with st.form("feedback"):
    rating = st.slider("Rate your experience", 1, 5, 3)
    category = st.selectbox("Category", ["General", "Technical", "Feature Request", "Bug Report"])
    comments = st.text_area("Comments")
    
    submitted2 = st.form_submit_button("Submit Feedback")
    
    if submitted2:
        st.success("✅ Feedback submitted!")
        st.write(f"Rating: {rating}/5")
        st.write(f"Category: {category}")
        st.write(f"Comments: {comments}")

        # Send feedback to PostgreSQL
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO feedback (rating, category, comments) VALUES (%s, %s, %s) RETURNING id",
                    (rating, category, comments)
                )
                result = cursor.fetchone()
                conn.commit()
                print(f"Feedback inserted with ID: {result[0]}")
                cursor.close()
                conn.close()
            except psycopg2.Error as e:
                print(f"Error inserting feedback: {e}")
                if conn:
                    conn.rollback()
                    conn.close()
        else:
            st.error("Failed to connect to database")