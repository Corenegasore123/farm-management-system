<div align="center">

# Farm Management System

[![Django](https://img.shields.io/badge/Django-4.2-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-informational)](#license)

Manage farmers, track attendance, and register students with a clean, Bootstrap-powered UI.

</div>

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Environment Variables](#environment-variables)
- [Run & Useful URLs](#run--useful-urls)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Django application streamlines day-to-day operations for small farms and co-ops. It lets you register farmers, record and view attendance, and now includes a polished Student Management portal to register and list students side-by-side with farmer data.

## Key Features

- **Attendance dashboard**: Recent farmer attendance at `/attendance/`.
- **Farmer management**:
  - List all farmers at `/attendance/farmers/`.
  - Add a farmer at `/attendance/farmers/add/`.
- **Student management portal**:
  - List all students at `/attendance/students/`.
  - Add a student at `/attendance/students/add/`.
- **Admin panel**: Full CRUD via `/admin/` after creating a superuser.
- **Modern UI**: Responsive layout using Bootstrap 5 and a minimal, readable design.

## Tech Stack

- Python 3.12, Django 4.2
- PostgreSQL (configurable via environment variables)
- Bootstrap 5 (CDN)

## Quick Start

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create `.env` in the project root (see [Environment Variables](#environment-variables)).
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser (optional, for `/admin/`):
   ```bash
   python manage.py createsuperuser
   ```
6. Start the server:
   ```bash
   python manage.py runserver
   ```

## Environment Variables

The app loads environment variables from `.env` (handled directly in `fms/settings.py`).

```env
# Core
DEBUG=True
SECRET_KEY=your-very-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=fms2
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432
```

## Run & Useful URLs

```bash
python manage.py runserver
```

- Attendance: `http://localhost:8000/attendance/`
- Farmers list: `http://localhost:8000/attendance/farmers/`
- Add farmer: `http://localhost:8000/attendance/farmers/add/`
- Students list: `http://localhost:8000/attendance/students/`
- Add student: `http://localhost:8000/attendance/students/add/`
- Admin: `http://localhost:8000/admin/`

## Project Structure

```
farm-management-system/
├─ attendance/
│  ├─ models.py            # Farmer, Attendance, Student
│  ├─ forms.py             # FarmerForm, StudentForm
│  ├─ views.py             # attendance_list, farmers_list, students_list, add_* views
│  ├─ urls.py              # App routes
│  ├─ templates/attendance/
│  │  ├─ base.html
│  │  ├─ attendance_list.html
│  │  ├─ farmers_list.html
│  │  ├─ students_list.html
│  │  └─ add_{farmer|student}.html
│  └─ static/attendance/css/styles.css
├─ fms/
│  ├─ settings.py          # Loads .env, DB config, CSRF & hosts
│  └─ urls.py              # Includes attendance URLs
├─ .env                    # Environment variables (ignored)
├─ requirements.txt        # Python dependencies
└─ manage.py
```

## Screenshots

- Attendance dashboard
- Farmers list / Add farmer
- Students list / Add student

Add screenshots to showcase the UI once you have them available.

## Roadmap

- Student attendance tracking (parallel to farmer attendance)
- Edit/delete flows for Farmers and Students (CRUD)
- Filtering, search, pagination
- Export reports (CSV/Excel)

## Contributing

- Fork the repo and create a feature branch.
- Add tests where appropriate.
- Open a pull request with a clear summary of changes.

## License

This project is licensed under the MIT License.
