import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="AI Grievance System", layout="centered")

st.title("🏛️ AI-Powered Citizen Grievance System")

st.markdown("""
Submit your complaint and the system will:
- 📌 Identify the department  
- ⚡ Detect urgency  
- 🚀 Assign priority score  
""")

# Input box
user_input = st.text_area("📝 Enter your complaint", height=150)

if st.button("Analyze Complaint"):

    if not user_input.strip():
        st.warning("Please enter a complaint.")
    else:
        with st.spinner("Analyzing..."):
            response = requests.post(API_URL, params={"text": user_input})

            if response.status_code == 200:
                result = response.json()

                st.success("Analysis Complete!")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("🏢 Department", result["department"])

                with col2:
                    st.metric("⚠️ Sentiment", result["sentiment"])

                # Priority visualization
                score = result["priority_score"]

                st.markdown("### 🚦 Priority Level")

                if score == 5:
                    st.error("🔴 CRITICAL - Immediate Action Required")
                elif score == 3:
                    st.warning("🟠 Moderate Priority")
                else:
                    st.info("🟢 Low Priority")

            else:
                st.error("API Error")