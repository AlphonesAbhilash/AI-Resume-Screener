from extract_text import get_extracted_text, analyze_resume_section, score_resume
import google.generativeai as genai

# 🔐 Gemini API key (already verified working)
genai.configure(api_key="AIzaSyBOEKypSs13c0gubWrZTVY85qDYXc2RMzQ")

# 📄 PDF File
pdf_path = "Alphones Resume.pdf"
text = get_extracted_text(pdf_path)
print("✅ Text extracted!")

# 📊 Section Detection + Score
found_sections = analyze_resume_section(text)
score = score_resume(found_sections)

# 🧾 Section Summary
section_summary = "\n📄 Resume Sections:\n"
for section, present in found_sections.items():
    mark = "✅" if present else "❌"
    section_summary += f"- {section}: {mark}\n"

# 🤖 Gemini Feedback Function
def get_resume_feedback(resume_text):
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
    return response.text

# 🧠 Get AI Feedback
gemini_feedback = get_resume_feedback(text)

# 🖨️ Final Report
print("\n============================")
print("✅ FINAL RESUME ANALYSIS 🔍")
print("============================\n")
print(f"📌 Structure-Based ATS Score: {score}/100")
print(section_summary)
print("🤖 Gemini Feedback:\n")
print(gemini_feedback)
