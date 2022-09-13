release: sh -c 'python manage.py migrate && python manage.py loaddata initial_catalog_data.json'
web: gunicorn tugas2-bimo-h.wsgi --log-file -