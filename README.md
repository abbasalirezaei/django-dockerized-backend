```markdown
# django-dockerized-backend 🐳

A production-ready Django starter kit powered by Docker, featuring:

- **Django** – backend framework  
- **PostgreSQL** – database  
- **Redis** – cache & Celery broker  
- **Celery** – async tasks & scheduled jobs  
- **Flower** – Celery monitoring dashboard  
- **SMTP4DEV** – local email testing  

This boilerplate provides a scalable and maintainable backend environment out-of-the-box — perfect for starting new projects with modern best practices.

---

## 🚀 Creating a New Django App

To create a new Django app (e.g., `todo`) and apply migrations inside the Dockerized environment:

### 1️⃣ Create the app inside the `apps/` directory

```bash
docker compose exec backend python manage.py startapp todo apps/todo
```

> Alternatively, for interactive shell:
```bash
docker compose exec -it backend sh -c "python manage.py startapp todo apps/todo"
```

### 2️⃣ Apply migrations

```bash
docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py migrate
```

### ✅ Register the app

Make sure to add the app to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'apps.todo',
]
```

---


```

---
