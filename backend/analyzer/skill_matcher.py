import spacy
nlp = spacy.load("en_core_web_sm")

def match_skills_and_score(resume_text, jd_text):
    skill_list = ["python", "machine learning", "react", "flask", "nlp", "deep learning", "data analysis", "sql"]
    matched = [skill for skill in skill_list if skill in resume_text]
    missing = [skill for skill in skill_list if skill not in resume_text and skill in jd_text]
    score = int((len(matched) / len(skill_list)) * 100)
    return score, missing, matched

def explain_score(score, matched_skills, missing_skills):
    explanation = f"Your resume matched {len(matched_skills)} out of {len(matched_skills) + len(missing_skills)} key skills."
    if score >= 80:
        explanation += "Great match! You're well-suited for this role."
    elif score >= 50:
        explanation += "Moderate match. Consider addressing some missing skills."
    else:
        explanation += "Low match. Enhancing your resume could help improve alignment."
    return explanation
