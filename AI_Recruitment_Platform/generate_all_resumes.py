from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        pass
    def footer(self):
        pass

def create_resume_pdf(role_name, type_name, skills_list, summary, experience):
    # type_name should be "Strong" or "Weak"
    filename = f"{role_name.replace(' ', '_')}_{type_name}_Resume.pdf"
    
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Header: Name
    name = f"JOHN {role_name.split()[0].upper()}" if type_name == "Strong" else f"TAYLOR {role_name.split()[0].upper()}"
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, name, ln=True, align='C')
    
    # Header: Contact Info
    pdf.set_font("Arial", '', 10)
    # The weak resume could be missing a LinkedIn/GitHub link to lower its score
    if type_name == "Strong":
        pdf.cell(0, 5, f"{role_name} | Email: john.strong@email.com | Location: Tech City", ln=True, align='C')
        pdf.cell(0, 5, f"LinkedIn: linkedin.com/in/johnstrong | GitHub: github.com/johnstrong", ln=True, align='C')
    else:
        pdf.cell(0, 5, f"Email: taylor.weak@email.com", ln=True, align='C')
    pdf.ln(5)
    
    def section_title(title):
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, title, ln=True, border='B')
        pdf.ln(2)

    # SUMMARY
    section_title("PROFESSIONAL SUMMARY")
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(0, 5, summary)
    pdf.ln(5)

    # SKILLS
    section_title("TECHNICAL SKILLS")
    pdf.set_font("Arial", '', 10)
    if skills_list:
        for skill in skills_list:
            pdf.cell(0, 5, f"- {skill}", ln=True)
    else:
        pdf.cell(0, 5, "Familiar with some basic software tools and typing.", ln=True)
    pdf.ln(5)

    # EXPERIENCE
    section_title("PROFESSIONAL EXPERIENCE")
    if experience:
        for exp in experience:
            pdf.set_font("Arial", 'B', 11)
            pdf.cell(0, 6, exp['title'], ln=True)
            pdf.set_font("Arial", 'I', 10)
            pdf.cell(0, 5, exp['dates'], ln=True)
            pdf.set_font("Arial", '', 10)
            for bullet in exp['bullets']:
                pdf.multi_cell(0, 5, f"- {bullet}")
            pdf.ln(3)
    else:
        pdf.multi_cell(0, 5, "Student looking for first professional experience.")
        pdf.ln(3)

    # EDUCATION
    section_title("EDUCATION")
    pdf.set_font("Arial", 'B', 11)
    if type_name == "Strong":
        pdf.cell(0, 6, "Bachelor of Science in Computer Science", ln=True)
        pdf.set_font("Arial", '', 10)
        pdf.cell(0, 5, "Graduated: May 2019 - Academic Excellence", ln=True)
    else:
        # Weak education section
        pdf.cell(0, 6, "High School Diploma", ln=True)
        pdf.set_font("Arial", '', 10)
        pdf.cell(0, 5, "Graduated: 2020", ln=True)
    pdf.ln(5)

    pdf.output(filename)
    print(f"Created {filename}")

if __name__ == "__main__":
    
    # ------------------- FRONTEND -------------------
    create_resume_pdf(
        "Frontend Developer", "Strong",
        ["HTML, CSS, JavaScript, TypeScript", "React, Vue.js, Angular, Next.js", "Redux, REST APIs, Webpack, Tailwind CSS", "Git, Jest, Cypress"],
        "Creative and detail-oriented Frontend Developer with 4 years of experience building responsive and highly interactive web applications. Expert in React and modern JavaScript. Passionate about UI/UX and optimizing web performance.",
        [{
            "title": "Frontend Engineer | WebTech Inc.",
            "dates": "Jan 2021 - Present",
            "bullets": [
                "Developed user interfaces using React and Redux, improving application speed by 30%.",
                "Collaborated with designers to implement pixel-perfect, responsive layouts using Tailwind CSS.",
                "Integrated RESTful APIs to fetch and display dynamic content."
            ]
        }]
    )
    
    create_resume_pdf(
        "Frontend Developer", "Weak",
        ["HTML, basic CSS"],
        "I am looking for a job to make web pages. I like computers.",
        [{
            "title": "Web Maker (Freelance)",
            "dates": "Last Year",
            "bullets": [
                "Made a webpage for a friend using HTML.",
                "Changed some colors."
            ]
        }]
    )

    # ------------------- BACKEND -------------------
    create_resume_pdf(
        "Backend Developer", "Strong",
        ["Python, Java, Node.js, Go", "Django, Spring Boot, Express.js", "SQL, PostgreSQL, MongoDB, Redis", "Docker, Kubernetes, AWS, microservices"],
        "Robust Backend Developer heavily experienced in designing scalable system architectures and secure APIs. Proficient in Python and Java environments. Proven ability to optimize database queries handling millions of rows.",
        [{
            "title": "Backend Software Engineer | ServerSolutions",
            "dates": "Feb 2020 - Present",
            "bullets": [
                "Architected and deployed highly scalable REST APIs using Python and Django.",
                "Optimized PostgreSQL queries, reducing standard load times by 40%.",
                "Containerized applications using Docker and deployed them to AWS ECS."
            ]
        }]
    )

    create_resume_pdf(
        "Backend Developer", "Weak",
        ["Python scripting"],
        "Seeking a backend job to learn more programming.",
        [{
            "title": "Student",
            "dates": "2021",
            "bullets": [
                "Wrote some python scripts.",
                "Looked at a SQL database once."
            ]
        }]
    )

    # ------------------- FULL STACK -------------------
    create_resume_pdf(
        "Full Stack Developer", "Strong",
        ["Python, JavaScript, TypeScript, Java", "React, Django, Node.js, Express.js", "SQL, PostgreSQL, MongoDB, AWS", "REST API, GraphQL, Docker, Jenkins"],
        "Versatile Full Stack Developer with 5 years of experience bridging the gap between elegant frontend interfaces and robust backend architectures. Capable of leading end-to-end web application development and deploying scalable solutions.",
        [{
            "title": "Full Stack Developer | OmniTech",
            "dates": "Mar 2019 - Present",
            "bullets": [
                "Led the development of a real-time analytics dashboard using React on the frontend and Node.js on the backend.",
                "Designed robust relational database schemas in PostgreSQL.",
                "Configured CI/CD pipelines using Jenkins to automate testing and deployment."
            ]
        }]
    )

    create_resume_pdf(
        "Full Stack Developer", "Weak",
        ["HTML, Python"],
        "Good developer looking for full stack roles.",
        [{
            "title": "Trainee | Local Business",
            "dates": "Summer 2022",
            "bullets": [
                "Fixed some bugs on the website.",
                "Helped with the backend occasionally."
            ]
        }]
    )

    # ------------------- DATA SCIENTIST -------------------
    create_resume_pdf(
        "Data Scientist", "Strong",
        ["Python, R, SQL, MATLAB", "TensorFlow, PyTorch, Scikit-Learn, Pandas", "Machine Learning, Deep Learning, NLP", "Tableau, AWS SageMaker, Hadoop"],
        "Innovative Data Scientist holding a strong background in statistical modeling, machine learning, and predictive analytics. Skilled in deploying complex ML models into production to drive critical business decisions.",
        [{
            "title": "Data Scientist | Insight Analytics",
            "dates": "Jun 2020 - Present",
            "bullets": [
                "Developed and deployed a customer churn prediction model using Random Forests, retaining $2M in revenue.",
                "Processed large datasets using Pandas and SQL to feed into Neural Networks using PyTorch.",
                "Applied Natural Language Processing (NLP) techniques to analyze customer feedback sentiment."
            ]
        }]
    )
    
    create_resume_pdf(
        "Data Scientist", "Weak",
        ["Excel, Math"],
        "I enjoy working with numbers and want to be a Data Scientist.",
        [{
            "title": "Trainee Data Entry",
            "dates": "2021",
            "bullets": [
                "Entered data into spreadsheets.",
                "Created pie charts using Microsoft Excel."
            ]
        }]
    )

    # ------------------- HR MANAGER -------------------
    create_resume_pdf(
        "Human Resources", "Strong",
        ["Talent Acquisition, Employee Relations, Onboarding", "HRIS (Workday, BambooHR), Applicant Tracking Systems", "Performance Management, Compliance", "Conflict Resolution, Payroll Administration"],
        "Dedicated Human Resources professional with 7 years of specialized experience in full-cycle recruiting, employee retention, and performance management. Strong advocate for company culture and organizational growth.",
        [{
            "title": "HR Manager | PeopleCorp",
            "dates": "Aug 2017 - Present",
            "bullets": [
                "Managed the full-cycle recruitment process, hiring over 200 software engineers in 2 years.",
                "Implemented a new ATS system that reduced time-to-hire by 15 days.",
                "Conducted performance reviews, conflict resolution, and compliance training for all employees."
            ]
        }]
    )

    create_resume_pdf(
        "Human Resources", "Weak",
        ["Talking to people, Organization"],
        "Looking to work in HR because I am a people person.",
        [{
            "title": "Front Desk Receptionist",
            "dates": "2019-2021",
            "bullets": [
                "Greeted guests when they arrived.",
                "Answered phone calls and managed calendars."
            ]
        }]
    )
