from extract_text import get_extracted_text
import google.generativeai as genai

# ✅ Use your working Gemini API key here
genai.configure(api_key="AIzaSyBOEKypSs13c0gubWrZTVY85qDYXc2RMzQ")

# 📝 Extracted text from resume
pdf_path = "Alphones Resume.pdf"
text = get_extracted_text(pdf_path)
print("✅ Text extracted!")

# 🤖 Gemini resume feedback
def get_resume_feedback(resume_text):
    model = genai.GenerativeModel("gemini-1.5-pro")  # 🔁 FIXED model name here!

    prompt = f"""
    You are an AI Resume Expert. Analyze the following resume and give:
    - An ATS (Applicant Tracking System) score out of 100
    - 3 strengths
    - 3 areas for improvement
    - 2 suggestions to make it more job-ready

    Resume Text:
    \"\"\"{resume_text}\"\"\"
    """

    response = model.generate_content(prompt)
    return response.text

# 🏁 Final output
if __name__ == "__main__":
    print("\n===== Resume Analysis =====\n")
    print(get_resume_feedback(text))
