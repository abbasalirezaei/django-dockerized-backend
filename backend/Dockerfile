FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy all requirement files
COPY requirements/ ./requirements/

# Install dependencies (dev environment by default)
RUN pip install --upgrade pip && pip install -r requirements/dev.txt

# Copy the entire backend code
COPY . .

# Run Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
