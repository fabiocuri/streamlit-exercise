import streamlit as st
from mongodb_script import client

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

        ## Send this information to mongodb

        database = client["test_database"]

        try:
            database.create_collection("example_collection")
        except:
            pass

        collection = database["example_collection"]

        # Save a text document
        document = {
            "name": name,
            "email": email
        }

        result = collection.insert_one(document)
        print(f"Document inserted with ID: {result.inserted_id}")

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