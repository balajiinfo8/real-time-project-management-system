

# 🚀 Django Task Manager (Production-Style Backend)

A scalable task management web application built with Django, featuring authentication, CRUD operations, and secure backend architecture. Designed to simulate real-world backend systems with clean structure and performance-focused implementation.

---

## 🔗 Live Demo

👉 https://task-manager-django-iqs0.onrender.com

---

## ⚙️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite / MySQL
* JWT Authentication
* Bootstrap (Crispy Forms)
* Linux Deployment (Render)

---

## ✨ Features

* 🔐 Secure User Authentication (Login / Logout)
* 📝 Full CRUD Task Management
* ⚡ Optimized database queries using Django ORM
* 🔁 JWT Token support for API authentication
* 🧠 CSRF protection & session security
* 🎯 Clean UI with Bootstrap forms

---

## 🧩 System Design

* Modular Django app architecture
* Separation of concerns (models, views, forms)
* Auth-protected views using decorators
* REST-ready backend with JWT endpoints

---

## 📂 Key Routes

| Route                 | Description   |
| --------------------- | ------------- |
| `/`                   | Login page    |
| `/home/`              | Dashboard     |
| `/del/<id>`           | Delete task   |
| `/edit/<id>`          | Edit task     |
| `/api/token/`         | JWT token     |
| `/api/token/refresh/` | Refresh token |

---

## ⚡ Backend Highlights

* Handles authenticated sessions and protected routes
* Efficient CRUD operations using Django ORM
* Integrated JWT authentication for API scalability
* Designed for extension into full REST backend

---

## 🛠️ Run Locally

```bash
git clone https://github.com/balajiinfo8/task_manager_django.git
cd task_manager_django

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📌 Future Improvements

* Docker-based deployment
* Role-based user system
* Notification & reminders
* API documentation (Swagger/OpenAPI)

---

## 👨‍💻 Author

**Balaji V**
Backend Engineer (Python | FastAPI | Real-Time Systems)

* GitHub: https://github.com/balajiinfo8
* LinkedIn: https://www.linkedin.com/in/balaji-vinothkumar/

---
