import streamlit as st
import requests


st.set_page_config(page_title="Email Verification Tool", page_icon="📧", layout="centered")
# Function to verify email
def verify_email(email):
    url = f"https://mailscrap.com/api/verifier-lookup/{email}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data", "status_code": response.status_code}

# Streamlit UI
st.title("📧 Email Verification Tool")

# User input
email = st.text_input("Enter Email Address:", "")

if st.button("Verify Email"):
    if email:
        data = verify_email(email)
        
        if "error" in data:
            st.error(f"Error: {data['error']} (Status Code: {data['status_code']})")
        else:
            # Create tabs for different details
            tab1, tab2, tab3 = st.tabs(["📜 Overview", "🔍 Email Properties", "🛠️ Server Info"])
            
            with tab1:
                st.subheader("📜 Overview")
                st.write(f"**Email:** {data.get('email', 'N/A')}")
                st.write(f"**Deliverable:** {'✅ Yes' if data.get('deliverable') else '❌ No'}")
                st.write(f"**Valid Format:** {'✅ Yes' if data.get('valid-format') else '❌ No'}")

            with tab2:
                st.subheader("🔍 Email Properties")
                st.write(f"**Disposable Email:** {'🚫 Yes' if data.get('disposable') else '✅ No'}")
                st.write(f"**Role-Based Email:** {'🚫 Yes' if data.get('role-base') else '✅ No'}")
                st.write(f"**Free Mail Provider:** {'✅ Yes' if data.get('free-mail') else '❌ No'}")

            with tab3:
                st.subheader("🛠️ Server Information")
                st.write(f"**Server Status:** {'🟢 Active' if data.get('server-status') else '🔴 Inactive'}")
                st.write(f"**Email Domain:** {data.get('email-domain', 'N/A')}")

    else:
        st.warning("⚠️ Please enter an email address to verify.")
