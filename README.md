# knowl
step 1: open terminal or cmd
pip install django
django-admin startproject user_portal
cd user_portal
python manage.py startapp file_manager

step 2: Add your app to the INSTALLED_APPS in user_portal/settings.py:
INSTALLED_APPS = [
    # ...
    'file_manager',
]

step 3: Start the development server:
python manage.py runserver

step 4: show output
http://127.0.0.1:8000
http://127.0.0.1:8000/dashboard/
http://127.0.0.1:8000/profile/sohel/
http://127.0.0.1:8000/search/
