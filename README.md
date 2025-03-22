📚 Library Management System
A Django-based RESTful API for managing library books and users.

🚀 Features
📖 Book Management: Add, update, delete, and list books.

👩‍🎓 Student Access: Students can view available books.

🔑 Authentication: Token-based authentication for admin and students.

🔐 Role-Based Access: Admins can perform CRUD operations, students can only read data.

📡 REST API: Built with Django REST Framework (DRF).

🛠 Database: MySQL as the backend database.

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