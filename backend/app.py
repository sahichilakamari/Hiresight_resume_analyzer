from flask import Flask, request, jsonify, send_file
from parser.resume_parser import extract_resume_text
from parser.job_parser import extract_jd_text
from analyzer.skill_matcher import match_skills_and_score, explain_score
from analyzer.suggester import generate_suggestions
from utils.report_generator import generate_pdf_report
from flask_cors import CORS
import tempfile

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    resume = request.files['resume']
    jd = request.files['jd']
    resume_text = extract_resume_text(resume)
    jd_text = extract_jd_text(jd)

    score, missing_skills, matched_skills = match_skills_and_score(resume_text, jd_text)
    suggestions = generate_suggestions(missing_skills, resume_text, jd_text)
    explanation = explain_score(score, matched_skills, missing_skills)

    response_data = {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions,
        "explanation": explanation
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
