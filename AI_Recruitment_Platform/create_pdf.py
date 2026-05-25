from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

def create_resume_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Header: Name
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "JANE DOE", ln=True, align='C')
    
    # Header: Contact Info
    pdf.set_font("Arial", '', 10)
    pdf.cell(0, 5, "Data Analyst | Email: jane.doe@email.com | Phone: (555) 123-4567 | Location: New York, NY", ln=True, align='C')
    pdf.cell(0, 5, "LinkedIn: linkedin.com/in/janedoe | GitHub: github.com/janedoe", ln=True, align='C')
    pdf.ln(5)
    
    def section_title(title):
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, title, ln=True, border='B')
        pdf.ln(2)

    # SUMMARY
    section_title("PROFESSIONAL SUMMARY")
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(0, 5, "Detail-oriented and analytical Data Analyst with 3+ years of experience in data gathering, processing, and statistical modeling. Proficient in transforming raw data into actionable business insights using Python, SQL, and Tableau. Strong track record of improving operational efficiency by 20% through data-driven recommendations and automated reporting.")
    pdf.ln(5)

    # SKILLS
    section_title("TECHNICAL SKILLS")
    pdf.set_font("Arial", '', 10)
    skills = [
        "- Programming Languages: Python (Pandas, NumPy, Scikit-learn), R, SQL",
        "- Database Management: MySQL, PostgreSQL, MongoDB, Snowflake",
        "- Data Visualization: Tableau, Power BI, Matplotlib, Seaborn",
        "- Statistical Analysis: A/B Testing, Predictive Modeling, Regression Analysis",
        "- Tools & Platforms: Excel (Advanced), Jupyter Notebook, Git, AWS"
    ]
    for skill in skills:
        pdf.cell(0, 5, skill, ln=True)
    pdf.ln(5)

    # EXPERIENCE
    section_title("PROFESSIONAL EXPERIENCE")
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(0, 6, "Data Analyst | TechVision Solutions - New York, NY", ln=True)
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(0, 5, "June 2021 - Present", ln=True)
    pdf.set_font("Arial", '', 10)
    exp1 = [
        "- Designed and maintained automated interactive Dashboards in Tableau, reducing manual reporting time by 15 hours per week.",
        "- Wrote complex SQL queries to extract, clean, and merge datasets from multiple relational databases containing over 5M records.",
        "- Conducted comprehensive A/B testing on marketing campaigns, resulting in a 15% increase in customer conversion rates.",
        "- Built a Python-based predictive model using Scikit-Learn to identify churn risks, improving customer retention by 12%."
    ]
    for line in exp1:
        pdf.multi_cell(0, 5, line)
    
    pdf.ln(4)
    
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(0, 6, "Junior Data Analyst | MarketTrend Analytics - Boston, MA", ln=True)
    pdf.set_font("Arial", 'I', 10)
    pdf.cell(0, 5, "September 2019 - May 2021", ln=True)
    pdf.set_font("Arial", '', 10)
    exp2 = [
        "- Cleaned and pre-processed large datasets using Python (Pandas, NumPy) to ensure data accuracy and integrity prior to analysis.",
        "- Generated weekly and monthly performance reports using Advanced Excel for stakeholders.",
        "- Analyzed consumer behavior trends and visualized findings using Power BI, influencing the Q4 product marketing strategy."
    ]
    for line in exp2:
        pdf.multi_cell(0, 5, line)
    pdf.ln(5)

    # EDUCATION
    section_title("EDUCATION")
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(0, 6, "Bachelor of Science in Computer Science | University of Massachusetts", ln=True)
    pdf.set_font("Arial", '', 10)
    pdf.cell(0, 5, "Graduated: May 2019", ln=True)
    pdf.multi_cell(0, 5, "Relevant Coursework: Data Mining, Probability and Statistics, Machine Learning, Database Design")
    pdf.ln(5)

    # PROJECTS & CERTIFICATIONS
    section_title("PROJECTS & CERTIFICATIONS")
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 5, "Sales Forecasting Model: Developed an ML pipeline in Python forecasting sales with 89% accuracy.", ln=True)
    pdf.cell(0, 5, "Customer Segmentation: Segmented 50K users using K-Means clustering and built a Power BI dashboard.", ln=True)
    pdf.ln(2)
    pdf.set_font("Arial", '', 10)
    pdf.cell(0, 5, "- Google Data Analytics Professional Certificate (2022)", ln=True)
    pdf.cell(0, 5, "- AWS Certified Cloud Practitioner (2021)", ln=True)

    pdf.output("Data_Analyst_Resume.pdf")
    print("PDF successfully created!")

if __name__ == "__main__":
    create_resume_pdf()
