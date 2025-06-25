# streamlit_app.py
# HireSight: AI-Powered Resume Gap Analyzer (Streamlit Version)

import streamlit as st
import requests
import json

st.set_page_config(page_title="HireSight - Resume Analyzer", page_icon="📄", layout="centered")
st.title("📄 HireSight")
st.subheader("AI-Powered Resume Gap Analyzer")

st.markdown("""
Upload your **Resume (PDF)** and a **Job Description (TXT)** file. This app will analyze your skill match, suggest improvements, and generate a downloadable report.
""")

resume_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
jd_file = st.file_uploader("Upload the Job Description (TXT)", type=["txt"])


if st.button("Analyze") and resume_file and jd_file:
    with st.spinner("Analyzing resume and job description..."):
        files = {"resume": resume_file, "jd": jd_file}
        response = requests.post("http://localhost:5000/analyze", files=files)

        if response.ok:
            result = response.json()
            st.session_state["analysis_result"] = result  # 🔐 Store in session
            st.success(f"✅ Match Score: {result['score']}%")
            st.markdown("**✔️ Matched Skills:**")
            st.write(", ".join(result["matched_skills"]))
            st.markdown("**❌ Missing Skills:**")
            st.write(", ".join(result["missing_skills"]))
            st.markdown("**💡 Suggestions:**")
            for tip in result["suggestions"]:
                st.write(f"- {tip}")
            st.markdown("**📊 Score Explanation:**")
            st.info(result["explanation"])
            