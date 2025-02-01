# BharatFD (FAQ Project)

This Django project provides a FAQ service with REST API support. Follow this guide to set up the project.

## Prerequisites

- Python 3.12+
- pip
- Virtual Environment (venv)
- Git

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/bharatfd.git
   cd bharatfd

   ```

2. **Create Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate

   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

   ```

4. **Run Migrations**

   ```bash
   python manage.py makemigrations
python manage.py migrate

   ```

5. **Create Superuser**

   ```bash
   python manage.py createsuperuser

   ```

6. **Run Server**

   ```bash
   python manage.py runserver


   ```

7. **view all Routes**

   ```bash
    python manage.py show_urls

   ```

8. **Run Test**

   ```bash
    python manage.py test

   ```

9. **Project Structure**

   ```bash
   ├── bharatfd
   │   ├── settings.py
   │   ├── urls.py
   │   └── wsgi.py
   ├── faq
   │   ├── admin.py
   │   ├── apps.py
   │   ├── models.py
   │   ├── serializers.py
   │   ├── tests.py
   │   ├── urls.py
   │   └── views.py
   ├── manage.py
   └── requirements.txt

   ```

10. **API USAGE**

```bash
curl http://localhost:8000/api/faqs/

# Fetch FAQs in Hindi
curl http://localhost:8000/api/faqs/?lang=hi

# Fetch FAQs in Bengali
curl http://localhost:8000/api/faqs/?lang=bn


```
