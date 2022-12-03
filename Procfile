release: python manage.py migrate
web: python manage.py migrate && python manage.py loaddata initial_wishlist_data.json && gunicorn project_django.wsgi 