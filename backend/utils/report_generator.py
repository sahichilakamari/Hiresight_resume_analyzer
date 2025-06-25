from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(40, 40, 80)
        self.cell(0, 10, "HireSight - Resume Match Report", ln=True, align="C")
        self.set_font("Arial", "I", 12)
        self.cell(0, 10, "AI-Powered Resume Gap Analyzer", ln=True, align="C")
        self.ln(10)

    def section_title(self, title):
        self.set_font("Arial", "B", 14)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def section_body(self, content):
        self.set_font("Arial", "", 12)
        self.set_text_color(50, 50, 50)
        if isinstance(content, list):
            for item in content:
                self.cell(0, 8, f"- {item}", ln=True)
        else:
            self.multi_cell(0, 8, content)
        self.ln(5)

def generate_pdf_report(filename, score, matched, missing, suggestions, explanation):
    pdf = PDFReport()
    pdf.add_page()

    pdf.section_title("Match Score")
    pdf.section_body(f"Your resume matches {score}% of the job requirements.")

    pdf.section_title("Matched Skills")
    pdf.section_body(matched)

    pdf.section_title("Missing Skills")
    pdf.section_body(missing)

    pdf.section_title("Suggestions")
    pdf.section_body(suggestions)

    pdf.section_title("Score Explanation")
    pdf.section_body(explanation)

    pdf.output(filename)
