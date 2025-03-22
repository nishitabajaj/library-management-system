📚 Library Management System

Overview

The Library Management System is a web application built using Django and Django REST Framework (DRF). It allows an admin to manage books through CRUD operations and enables students to view available books. The system uses MySQL as the database and implements token-based authentication.

Features

Admin Authentication: Signup and login using email and password.

Book Management (Admin Only):

Add a new book.

Retrieve all books.

Update book details.

Delete a book.

Student View: Students can view all available books.

Token-Based Authentication: Secure access using JWT tokens.

🏗 Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/nishitabajaj/library-management-system.git

cd library-management-system

2️⃣ Create a virtual environment

python -m venv venv

source venv/bin/activate  # Mac/Linux

venv\Scripts\activate      # Windows


3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Configure database

Make sure MySQL is running, then update settings.py with your database credentials.

5️⃣ Run migrations

python manage.py migrate

6️⃣ Create a superuser (Admin)

python manage.py createsuperuser

7️⃣ Start the server

python manage.py runserver

📌 API Endpoints

Method	           Endpoint	           Description	          Access

POST	         /api/token/	Get access & refresh token	All Users

GET	             /api/books/	    List all books	        All Users

POST	         /api/books/	    Add a new book	          Admin

GET	            /api/books/<id>/	Retrieve book details	All Users

PUT	            /api/books/<id>/	Update book details       Admin

DELETE	        /api/books/<id>/	Delete a book             Admin


🛡 Authentication

Use JWT token for authentication:

1️⃣ First, login to get tokens:

POST /api/token/


2️⃣ Use the access token in the headers:

Authorization: Bearer <your_access_token>

🎯 Contributing

Pull requests are welcome! Fork the repository and submit a PR.