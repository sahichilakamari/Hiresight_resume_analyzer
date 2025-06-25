# 🚀 HireSight
### AI-Powered Resume Gap Analyzer

HireSight is an AI-driven web application that analyzes a resume against a job description, identifies skill gaps, calculates a match score, and generates actionable suggestions — complete with a downloadable PDF report.

---

## 📦 Features
- Resume & JD file upload (PDF/TXT)
- Skill matching using NLP (spaCy)
- Match score and missing skills
- Suggestions to improve job fit
- Beautiful PDF report generation
- Streamlit UI for fast deployment

---

## 🛠️ Tech Stack
- **Frontend/UI:** Streamlit
- **Backend:** Flask (served locally)
- **NLP:** spaCy, scikit-learn
- **PDF Parsing:** PyMuPDF
- **Report Generation:** FPDF

---

## 🖥️ Local Setup

```bash
# Clone the repo
https://github.com/yourusername/hiresight.git
cd hiresight

# Install dependencies
pip install -r requirements.txt

# Run Flask backend (in one terminal)
python backend/app.py

# Run Streamlit frontend (in another terminal)
streamlit run streamlit_app.py
```

> ⚠️ Note: Replace `http://localhost:5000` in `streamlit_app.py` if deploying backend elsewhere.

---

## ☁️ One-Click Deploy (Streamlit Cloud)
Deploy easily using the button below:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)

> ⚠️ Make sure your backend is deployed via Render, Heroku, or similar if running Streamlit on cloud.

---

## 📄 Sample Output
![Screenshot](docs/sample_output.png)

---

## 👨‍💻 Author
**Your Name**  
Built using Python, NLP, and a touch of design thinking ✨

---

## 📃 License
[MIT](LICENSE)
