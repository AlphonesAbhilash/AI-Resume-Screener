import fitz
import re

def extract_text_from_pdf(pdf_path):
    text=""

    doc=fitz.open(pdf_path)

    for page in doc:
        text+=page.get_text()

    doc.close()
    return text

def analyze_resume_section(text):

    sections={
        'Education':False,
        'Experience':False,
        'Skills':False,
        'Certification':False,
        'Projects':False
    }

    lowered_text=text.lower()

    for section in sections:
        pattern=section.lower()

        if re.search(pattern,lowered_text):
            sections[section]=True

    return sections

def score_resume(found_sections):
    score=0
    weights={
        'Education':20,
        'Experience':20,
        'Certification':20,
        'Projects':20,
        'Skills':20
    }

    for section,present in found_sections.items():
        if present and section in weights:
            score+=weights[section]

    return score

def get_extracted_text(pdf_path):
    return extract_text_from_pdf(pdf_path)


if __name__=="__main__":
    pdf_path="Alphones Resume.pdf"
    extracted_text=extract_text_from_pdf(pdf_path)
    print(extracted_text)

    found_sections=analyze_resume_section(extracted_text)
    print('\n Resume Section Analysis:\n')
    for section,present in found_sections.items():
        status="✅ Found" if present else "❌ Missing"
        print(f'{section}: {status}')
    sections = analyze_resume_section(extracted_text)
    score=score_resume(sections)

    print(f'Your Total Score: {score}/100')

# Key: AIzaSyBOEKypSs13c0gubWrZTVY85qDYXc2RMzQ