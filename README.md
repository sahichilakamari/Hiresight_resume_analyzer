# 🚀 HireSight
### AI-Powered Resume Gap Analyzer

HireSight is an AI-driven web application that analyzes a resume against a job description, identifies skill gaps, calculates a match score, and generates actionable suggestions — complete with a downloadable PDF report.

---

## 📦 Features
- Resume & JD file upload (PDF/TXT)
- Skill matching using NLP (spaCy)
- Match score and missing skills
- Suggestions to improve job fit
- Streamlit UI for fast deployment

---

## 🛠️ Tech Stack
- **Frontend/UI:** Streamlit
- **Backend:** Flask (served locally)
- **NLP:** spaCy, scikit-learn
- **PDF Parsing:** PyMuPDF

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

