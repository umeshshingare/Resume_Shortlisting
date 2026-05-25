import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_config.settings')
django.setup()

from dashboard.models import Job

def add_test_jobs():
    jobs_data = [
        {
            "title": "Frontend Developer",
            "company": "WebTech Inc.",
            "location": "New York, NY",
            "salary": "90000",
            "experience": "3+ years",
            "description": "We are looking for a creative Frontend Developer with deep expertise in React and modern JavaScript. You will build highly responsive, performance-optimized, user-facing applications.",
            "required_skills": "HTML, CSS, JavaScript, React, Tailwind CSS"
        },
        {
            "title": "Backend Software Engineer",
            "company": "ServerSolutions",
            "location": "San Francisco, CA",
            "salary": "110000",
            "experience": "4+ years",
            "description": "Seeking a robust Backend Engineer heavily experienced in scaling architectures and securing APIs. You will deploy REST APIs and optimize database structures carrying millions of rows.",
            "required_skills": "Python, Django, PostgreSQL, Docker, AWS"
        },
        {
            "title": "Full Stack Developer",
            "company": "OmniTech Global",
            "location": "Austin, TX (Hybrid)",
            "salary": "120000",
            "experience": "5+ years",
            "description": "A versatile Full Stack Developer needed to bridge the gap between frontend interfaces and backend architectures. You will deploy scalable full-stack web applications and microservices.",
            "required_skills": "Python, React, Node.js, SQL, Docker"
        },
        {
            "title": "Data Scientist",
            "company": "Insight Analytics",
            "location": "Boston, MA",
            "salary": "130000",
            "experience": "3+ years",
            "description": "Looking for an innovative Data Scientist with a strong background in Machine Learning and predictive models. You will produce real-time insights from company data pipelines.",
            "required_skills": "Python, SQL, Machine Learning, TensorFlow, Pandas"
        },
        {
            "title": "Human Resources Manager",
            "company": "PeopleCorp",
            "location": "Chicago, IL",
            "salary": "85000",
            "experience": "5+ years",
            "description": "Seeking a dedicated HR Manager for full-cycle recruiting and performance management. You must have prior experience heavily utilizing Applicant Tracking Systems and scaling company culture.",
            "required_skills": "Talent Acquisition, Employee Relations, HRIS, Compliance"
        }
    ]

    for data in jobs_data:
        # Avoid creating exact duplicates
        if not Job.objects.filter(title=data["title"], company=data["company"]).exists():
            Job.objects.create(**data)
            print(f"Added Job: {data['title']} at {data['company']}")
        else:
            print(f"Skipped Job (already exists): {data['title']} at {data['company']}")

if __name__ == "__main__":
    add_test_jobs()
    print("Test jobs population complete!")
