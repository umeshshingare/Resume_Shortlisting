# AI Recruitment Platform

## 1. Project Summary

`AI_Recruitment_Platform` is a Django-based recruitment automation system built to analyze resumes, classify candidates, recommend jobs, and provide an HR dashboard for applicant management.

The platform combines:
- Resume parsing and text extraction
- Natural Language Processing (NLP)
- Supervised and multi-label classification
- Job matching and recommendation
- Web-based candidate and HR interfaces

## 2. Key Features

- Candidate resume upload and AI-driven analysis
- Resume scoring using heuristic and ML-based features
- Skill extraction from uploaded resumes
- Job recommendation based on candidate profile
- HR dashboard for creating jobs, viewing applicants, and shortlisting
- Integrated job scraping support via Selenium
- Support for multi-label category prediction

## 3. Technology Stack

### Backend
- Python 3.x
- Django 4.x
- SQLite (development database)

### Machine Learning & NLP
- Scikit-Learn
- SpaCy
- NLTK
- SentenceTransformers / Hugging Face
- Pandas, NumPy
- joblib for model serialization

### PDF and Data Processing
- PyPDF2
- pdfminer.six
- pyresparser

### Frontend
- HTML5
- Bootstrap CSS
- Django templates

### Utilities
- Selenium for web scraping
- python-dotenv for environment variables
- matplotlib / seaborn for training visualization

## 4. Architecture Overview

The application follows Django's Model-View-Template (MVT) architecture.

### Main layers
- Presentation layer: HTML templates and Bootstrap UI served by Django views.
- Application layer: Django views, forms, and URL routing.
- Data layer: Django models persisted in SQLite.
- AI layer: Resume prediction and scoring logic in `app/prediction.py`.

## 5. File and Folder Structure

```text
AI_Recruitment_Platform/
├── add_test_jobs.py          # Script to add sample jobs
├── create_pdf.py             # Utility for PDF processing
├── create_superuser.py       # Helper to create a Django superuser
├── db.sqlite3                # SQLite database file
├── generate_all_resumes.py   # Generates resumes for the dataset
├── manage.py                 # Django CLI entrypoint
├── media/                    # Uploaded media files (resumes)
├── project_config/           # Django project configuration
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Root URL configuration
│   └── wsgi.py               # WSGI application
├── requirements.txt          # Python dependency list
├── static/                   # Static assets (CSS/JS)
│   └── css/style.css
├── templates/                # HTML templates for web pages
├── training/                 # ML model training scripts and artifacts
│   ├── model.pkl
│   ├── model_multilabel.pkl
│   ├── vectorizer.pkl
│   ├── vectorizer_multilabel.pkl
│   ├── encoder.pkl
│   ├── encoder_multilabel.pkl
│   ├── train_model.py
│   └── predict_multilabel.py
├── app/                      # Candidate-facing app logic
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── models.py
│   ├── prediction.py         # ML and resume scoring logic
│   ├── scrape_jobs.py        # Job scraping utilities
│   ├── urls.py
│   └── views.py
├── dashboard/                # HR dashboard and management app
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── README.md                 # Project README and usage instructions
```

### Template overview
- `templates/index.html` - Landing page
- `templates/register.html` / `templates/login.html` - Candidate auth
- `templates/dashboard.html` / `templates/hr_dashboard.html` - Dashboards
- `templates/resume.html` / `templates/resume_analysis.html` - Resume upload and AI output
- `templates/job_list.html` / `templates/job_card.html` - Jobs display
- `templates/applicant_detail.html` / `templates/job_applications_list.html` - Applicant workflows

## 6. Workflow

### 6.1 Setup Workflow

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
2. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Train or refresh ML models if needed:
   ```bash
   python training/train_model.py
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

### 6.2 Runtime Workflow

1. Candidate registers or logs in.
2. Candidate uploads a resume or fills profile details.
3. The resume text is extracted, cleaned, and passed through the ML prediction pipeline.
4. The platform predicts job categories, extracts skills, and computes a resume score.
5. Candidate sees recommended jobs and AI analysis results.
6. HR users create jobs, view applicants, and manage applications through the dashboard.

### 6.3 Training Workflow

1. Prepare datasets in `dataset/`.
2. Run `training/train_model.py` to build and save model artifacts.
3. Trained artifacts are saved to `training/` as `*.pkl` files.
4. The app loads these pickled artifacts for inference in `app/prediction.py`.

### 6.4 Developer Workflow

1. Edit views, models, or templates as needed.
2. Add or update datasets and retrain models.
3. Run migrations after model or schema changes.
4. Test locally with `python manage.py runserver`.

## 7. Important Notes

- `project_config/settings.py` uses SQLite and serves static files from `static/`.
- Uploaded resumes are stored in `media/resumes/`.
- The project uses `django_browser_reload` middleware for live reload during development.
- The `training/` folder already contains saved ML artifacts, but they may need retraining if you change dataset or feature logic.
- The `app/prediction.py` file is the key AI integration point. It loads models and performs resume scoring.

## 8. How to Use

- Visit `http://127.0.0.1:8000/` to open the site.
- Create a superuser for HR access:
  ```bash
  python manage.py createsuperuser
  ```
- Upload resumes and review predicted categories and scores.
- Manage jobs and applicants through the HR dashboard.

## 9. Extension Points

- Add new job categories and update dataset labels.
- Replace the current classifier with a transformer-based model.
- Improve resume parsing with additional PDF or DOCX parsers.
- Add email notifications and asynchronous task queues.
- Switch production database to PostgreSQL.
