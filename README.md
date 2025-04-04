# ✅ QuickTask API

QuickTask API is a minimal Django REST API project that allows users to add tasks and view them. It's a great starting point for anyone learning how to build APIs with Django and Django REST Framework.

---

## 🚀 Features

- Add tasks using a POST request
- View all added tasks via GET request
- Django Admin access for managing tasks

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/quicktask-api.git
cd quicktask-api
```

### 2. Create and activate virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

### 3. Install dependencies
```bash
pip install django djangorestframework
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
| :---:  |   :---:  |     :---:   |
| GET    | /api/tasks/ | List all tasks |
| POST   | /api/tasks/ | Add a new task |

## 📝 Sample JSON (POST)

```bash
{
  "title": "Finish Django project"
}
```

## 🧑‍💻 Author
⚡️Built by Poshika mangai M
