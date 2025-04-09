from flask import Flask, render_template, request
from extract_text import get_extracted_text, analyze_resume_section, score_resume
import google.generativeai as genai
import os

# ✅ Configure Gemini API
genai.configure(api_key="AIzaSyBOEKypSs13c0gubWrZTVY85qDYXc2RMzQ")

# ✅ Initialize Flask app
app = Flask(__name__)

# ✅ Route: Home page (GET shows upload form, POST handles resume processing)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["resume"]

        if uploaded_file.filename != "":
            # Save uploaded file temporarily
            file_path = os.path.join("temp_" + uploaded_file.filename)
            uploaded_file.save(file_path)

            # 1. Extract resume text
            resume_text = get_extracted_text(file_path)

            # 2. Analyze structure
            found_sections = analyze_resume_section(resume_text)
            ats_score = score_resume(found_sections)

            # 3. Get Gemini feedback
            model = genai.GenerativeModel("gemini-1.5-pro")
            prompt = f"""
            You are an AI Resume Expert. Analyze the following resume and provide:
            - An ATS score out of 100
            - 3 strengths of the resume
            - 3 weaknesses or areas for improvement
            - 2 suggestions to improve job-readiness

            Resume:
            \"\"\"{resume_text}\"\"\"
            """
            response = model.generate_content(prompt)
            ai_feedback = response.text

            # Delete file after processing
            os.remove(file_path)

            # Render results page
            return render_template("index.html", ats_score=ats_score, sections=found_sections, ai_feedback=ai_feedback)

    return render_template("index.html", ats_score=None, sections=None, ai_feedback=None)


# ✅ Run the app
if __name__ == "__main__":
    app.run(debug=True)