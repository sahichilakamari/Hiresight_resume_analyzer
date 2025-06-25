import spacy
from difflib import get_close_matches

nlp = spacy.load("en_core_web_sm")

def detect_resume_sections(text):
    sections = {
        "skills": [],
        "projects": [],
        "education": [],
        "experience": [],
    }

    lines = text.lower().splitlines()
    current = None

    for line in lines:
        if "project" in line:
            current = "projects"
        elif "skill" in line:
            current = "skills"
        elif "education" in line:
            current = "education"
        elif "experience" in line:
            current = "experience"

        if current and line.strip():
            sections[current].append(line.strip())

    return sections

def generate_suggestions(missing_skills, resume_text, jd_text):
    suggestions = []
    sections = detect_resume_sections(resume_text)
    resume_doc = nlp(resume_text)
    jd_doc = nlp(jd_text)

    jd_phrases = [chunk.text.lower() for chunk in jd_doc.noun_chunks]

    for skill in missing_skills:
        skill_lower = skill.lower()
        used_in_jd = any(skill_lower in phrase for phrase in jd_phrases)
        matched_section = ""

        for section, lines in sections.items():
            for line in lines:
                if skill_lower in line:
                    matched_section = section
                    break
            if matched_section:
                break

        if matched_section:
            suggestion = f"The skill '{skill}' is relevant to the '{matched_section}' section in your resume. Make sure it’s clearly described with examples or tools used."
        elif used_in_jd:
            suggestion = f"'{skill}' is a key requirement in the job description but not found in your resume. Consider adding it in your Skills section or in relevant Projects if you've worked on it."
        else:
            suggestion = f"Consider including '{skill}' in your resume if you have experience — it strengthens alignment with general industry expectations."

        # Bonus: Suggest section based on type
        tech_keywords = ["python", "sql", "tensorflow", "java", "git", "docker"]
        soft_keywords = ["teamwork", "communication", "leadership"]
        cloud_keywords = ["aws", "azure", "gcp"]

        if skill_lower in tech_keywords:
            suggestion += " You could add this under 'Technical Skills' or 'Projects'."
        elif skill_lower in soft_keywords:
            suggestion += " Add this under 'Achievements' or describe it in project outcomes."
        elif skill_lower in cloud_keywords:
            suggestion += " If you used this in projects or labs, list it under 'Skills' or 'Certifications'."

        suggestions.append(suggestion)

    return suggestions
