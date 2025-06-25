def extract_jd_text(file):
    text = file.read().decode("utf-8")
    return text.lower()
