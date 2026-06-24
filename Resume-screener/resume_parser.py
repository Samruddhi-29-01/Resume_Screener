skills_list = [
    "python",
    "java",
    "mysql",
    "html",
    "css",
    "javascript",
    "c programming",
    "cybersecurity"
]

def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills