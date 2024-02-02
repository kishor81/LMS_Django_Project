LMS
This is a Django-based Library Management System with RESTful APIs for managing books, users, and book borrowing.

Setup Instructions
1. Clone the Repository

2. Set Up Virtual Environment 
python -m venv venv venv\Scripts\activate

3. Install Dependencies 
pip install -r requirements.txt

4. Configure Database Update the database configuration in lms/settings.py with following MySQL credentials:

DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'LMS', 
        'USER': 'admin',
        'PASSWORD': '12345', 
        'HOST': 'localhost', 
        'PORT': '3306', 
        }
    }

5. Apply Migrations
    python manage.py makemigrations 
    python manage.py migrate

6. Create Superuser (Optional) 
    python manage.py createsuperuser

7. Run the Development Server 
    python manage.py runserver 
    The server will be accessible at http://127.0.0.1:8000/ by default.

Additional Note 
Ensure that MySQL is installed and running before setting up the project.