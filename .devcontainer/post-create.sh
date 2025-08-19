#!/bin/bash

# Install Python deps for Django backend
pip install --upgrade pip
pip install django djangorestframework django-channels redis ib_insync stripe firebase-admin onfido ccxt django-ratelimit celery pytest pytest-django

# Install Node deps for React frontend
cd /workspace/frontend  # Assuming your React code is in a 'frontend' folder
npm install

# Set up Django (assuming backend in 'backend' folder)
cd /workspace/backend
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput  # Or manual setup

# Generate sample data (as per your prompt)
python manage.py loaddata sample_data.json  # Add your fixtures

echo "Environment setup complete! Run 'python manage.py runserver' for Django and 'npm start' for React."
