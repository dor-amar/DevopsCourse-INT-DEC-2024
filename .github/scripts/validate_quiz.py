import os
import re
import json
import sys

# Get the quiz file name dynamically from the GitHub Actions environment
quiz_file = os.getenv("QUIZ_FILE", "quizzes/linux-quiz-1.md")

# Derive the answers file name from the quiz file name
answers_file = quiz_file.replace("quizzes/", "answers/").replace(".md", ".json")

# Ensure both files exist
if not os.path.exists(quiz_file):
    print(f"❌ Quiz file not found: {quiz_file}")
    sys.exit(1)

if not os.path.exists(answers_file):
    print(f"❌ Answers file not found: {answers_file}")
    sys.exit(1)

# Read the correct answers
with open(answers_file, "r") as f:
    correct_answers = json.load(f)

# Read the quiz file
with open(quiz_file, "r") as f:
    quiz_content = f.readlines()

# Extract submitted answers from the Markdown file
submitted_answers = {}
question_number = 0
for line in quiz_content:
    print(f"Processing line: {line.strip()}")  # Debugging line
    # Match lines with checkboxes and answers (e.g., "- [X] a) `mkdir`")
    match = re.match(r"^\s*-\s*\[\s*[xX]\s*\]\s*(\w)\)", line.strip())
    if match:
        question_number += 1
        submitted_answers[str(question_number)] = match.group(1).lower()

# Validate answers
correct_count = 0
for question, correct_answer in correct_answers.items():
    submitted_answer = submitted_answers.get(question, "none")
    if submitted_answer == correct_answer:
        correct_count += 1
    else:
        print(f"❌ Question {question}: Expected '{correct_answer}', but got '{submitted_answer}'")

# Print final result
if correct_count == len(correct_answers):
    print(f"✅ All {correct_count}/{len(correct_answers)} answers are correct!")
    sys.exit(0)
else:
    print(f"⚠️ {correct_count}/{len(correct_answers)} answers are correct.")
    sys.exit(1)
