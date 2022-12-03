release: python manage.py migrate && python manage.py loaddata initial_wishlist_data.json
web: python manage.py migrate && gunicorn project_django.wsgi 