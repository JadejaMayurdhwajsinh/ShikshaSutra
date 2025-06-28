# 🎓 ShikshaSutra

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-success)
![Top Language](https://img.shields.io/github/languages/top/your-username/ShikshaSutra?logo=python&color=blue)

**ShikshaSutra** (शिक्षा सूत्र) is a lightweight **Student Management System** built using **Python (Django)** as the backend and a fully custom **HTML + CSS** frontend.  
It allows users to register, log in, and manage student records with full **CRUD** functionality – without using Django’s default admin panel.

---

## 🚀 Features

- 🔐 User Login & Registration
- 📄 Add / Edit / Delete / View Students
- 🧾 Simple custom forms (no Django admin)
- 🎨 Clean HTML + CSS UI
- 🔒 Secure session-based access

---

## 🛠️ Tech Stack

| Technology | Description |
|------------|-------------|
| Python     | Programming language |
| Django     | Web framework |
| SQLite     | Lightweight DB (default) |
| HTML + CSS | Frontend UI |
| Git + GitHub | Version control & hosting |

---

## 💻 Local Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/ShikshaSutra.git
cd ShikshaSutra

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the server
python manage.py runserver
