# Farm Management System

Simple Django application to manage farmers and track attendance, now enhanced with a Student Management portal for registering and listing students alongside farmer records.

## Features

- **Attendance dashboard**: View recent farmer attendance records at `/attendance/`.
- **Farmer management**:
  - List all farmers at `/attendance/farmers/`.
  - Add a farmer at `/attendance/farmers/add/`.
- **Student management portal**:
  - List all students at `/attendance/students/`.
  - Add a student at `/attendance/students/add/`.
- **Admin panel**: Manage data from Django Admin at `/admin/` (after creating a superuser).

## Tech Stack

- Python 3.12, Django 4.2
- PostgreSQL (configurable via environment variables)
- Bootstrap 5 (CDN)

## Setup

1. Create and activate a virtual environment.
2. Install dependencies (if you have a requirements file):
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables in `.env` (already supported by `fms/settings.py`):
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=localhost,127.0.0.1
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=fms2
   DB_USER=postgres
   DB_PASSWORD=your-db-password
   DB_HOST=localhost
   DB_PORT=5432
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser (optional, for admin):
   ```bash
   python manage.py createsuperuser
   ```

## Run

```bash
python manage.py runserver
```

## URLs

- Attendance: `http://localhost:8000/attendance/`
- Farmers list: `http://localhost:8000/attendance/farmers/`
- Add farmer: `http://localhost:8000/attendance/farmers/add/`
- Students list: `http://localhost:8000/attendance/students/`
- Add student: `http://localhost:8000/attendance/students/add/`
- Admin: `http://localhost:8000/admin/`

## Notes

- CSRF is enabled; if you log in or switch hosts (localhost vs 127.0.0.1), refresh forms before POSTing.
- Local development trusts `localhost` and `127.0.0.1` by default via settings.
