# 🚀 Real-Time Project Management System

A full-stack Project Management System built with **Django REST Framework** and **React (Vite)**. The application allows users to securely manage projects and tasks using JWT authentication while providing a modern frontend and scalable REST APIs.

> **Project Status:** 🚧 Active Development

---

## ✨ Features

### Backend (Completed)

- JWT Authentication (Login & Registration)
- Secure REST APIs using Django REST Framework
- Project CRUD Operations
- Task CRUD Operations
- PostgreSQL Database Integration
- Input Validation
- Error Handling
- Modular API Architecture

### Frontend (In Progress)

- React (Vite)
- Responsive Dashboard
- Authentication Pages
- Project Management UI
- Task Management UI
- Real-Time Task Updates (Planned)

---

## 🛠️ Tech Stack

### Backend

- Python
- Django
- Django REST Framework
- JWT Authentication
- PostgreSQL

### Frontend

- React.js (Vite)
- HTML5
- CSS3
- JavaScript (ES6+)
- Bootstrap

### Tools

- Git
- GitHub
- Postman
- VS Code

---

## 📁 Project Structure

```
real-time-project-management-system
│
├── backend
│   ├── Django
│   ├── DRF
│   ├── APIs
│   └── PostgreSQL
│
├── frontend
│   ├── React (Vite)
│   ├── Components
│   ├── Pages
│   └── Services
│
└── README.md
```

---

## 🔐 Authentication

- User Registration
- User Login
- JWT Access Token
- JWT Refresh Token
- Protected API Endpoints

---

## 📋 Current Features

- Create Project
- View Projects
- Update Project
- Delete Project

- Create Task
- View Tasks
- Update Task
- Delete Task

---

## 🚧 Planned Features

- Task Status Management
- Task Priority
- Search & Filter
- Pagination
- User Profile
- Dashboard Analytics
- Real-Time Task Synchronization
- Team Collaboration
- Notifications

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/real-time-project-management-system.git
```

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /api/register/ | Register User |
| POST | /api/login/ | Login |
| GET | /api/projects/ | Get Projects |
| POST | /api/projects/ | Create Project |
| PUT | /api/projects/{id}/ | Update Project |
| DELETE | /api/projects/{id}/ | Delete Project |
| GET | /api/tasks/ | Get Tasks |
| POST | /api/tasks/ | Create Task |
| PUT | /api/tasks/{id}/ | Update Task |
| DELETE | /api/tasks/{id}/ | Delete Task |

---

## 📸 Screenshots

> Screenshots will be added after the frontend is completed.

---

## 🌐 Live Demo

Frontend: Coming Soon

Backend API: Coming Soon

---

## 👨‍💻 Author

**Balaji Vinothkumar**

- LinkedIn: https://linkedin.com/in/balaji-vinothkumar
- GitHub: https://github.com/balajiinfo8

---

## ⭐ Future Improvements

- Docker Support
- Redis Caching
- Celery Background Tasks
- Email Notifications
- AWS Deployment
- CI/CD with GitHub Actions
