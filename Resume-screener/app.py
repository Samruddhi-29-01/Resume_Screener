import os
import sqlite3

from pdf_reader import extract_text
from resume_parser import extract_skills
from scorer import calculate_score

job_skills = [
    "python",
    "java",
    "mysql",
    "git"
]

results = []

# Database Connection
conn = sqlite3.connect("resume.db")
cursor = conn.cursor()

# Create Table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resume_name TEXT,
    score REAL
)
""")

resume_folder = "resumes"

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        path = os.path.join(resume_folder, file)

        text = extract_text(path)

        candidate_skills = extract_skills(text)

        score, matched, missing = calculate_score(
            candidate_skills,
            job_skills
        )

        results.append({
            "name": file,
            "score": score,
            "matched": matched,
            "missing": missing
        })

        # Save to Database
        cursor.execute("""
        INSERT INTO candidates (resume_name, score)
        VALUES (?, ?)
        """, (file, score))

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\n===== CANDIDATE RANKING =====\n")

rank = 1

for candidate in results:

    print(f"Rank {rank}")
    print("Resume:", candidate["name"])
    print("Score:", candidate["score"], "%")
    print("Matched Skills:", candidate["matched"])
    print("Missing Skills:", candidate["missing"])
    print("---------------------------")

    rank += 1

conn.commit()
conn.close()