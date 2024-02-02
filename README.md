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

API Documentation
User APIs
Create a New User:

Endpoint: /api/create-user/
Method: POST
Request Body: {"Name": "ram", "Email": "ram@gmail.com", "MembershipDate": "2024-02-02"}
List All Users:

Endpoint: /api/list-all-users/
Method: GET
Get User by ID:

Endpoint: /api/get-user-by-id/{user_id}/
Method: GET
Book APIs
Add a New Book:

Endpoint: /api/add-new-book/
Method: POST
Request Body: {"Title": "New Book", "ISBN": "1234567890123", "PublishedDate": "2024-02-01", "Genre": "Fiction"}
List All Books:

Endpoint: /api/list-all-books/
Method: GET
Get Book by ID:

Endpoint: /api/get-book-by-id/{book_id}/
Method: GET
Assign/Update Book Details:

Endpoint: /api/assign-update-book-details/{book_id}/
Method: PUT
Request Body: {"NumberOfPages": 300, "Publisher": "Book Publisher", "Language": "English"}
BorrowedBooks APIs
Borrow a Book:

Endpoint: /api/borrow-book/
Method: POST
Request Body: {"UserID": "{user_id}", "BookID": "{book_id}", "BorrowDate": "2024-02-01"}
Return a Book:

Endpoint: /api/return-book/
Method: POST
Request Body: {"UserID": "{user_id}", "BookID": "{book_id}", "ReturnDate": "2022-02-01"}
List All Borrowed Books:

Endpoint: /api/list-all-borrowed-books/
Method: GET
