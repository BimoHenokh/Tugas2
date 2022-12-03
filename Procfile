release: python manage.py migrate
web: python manage.py migrate && gunicorn project_django.wsgi && python manage.py loaddata initial_wishlist_data.json