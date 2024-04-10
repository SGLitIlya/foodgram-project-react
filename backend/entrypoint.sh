python manage.py migrate --no-input
python manage.py loaddata fixture.json
python manage.py load_ingredients
python manage.py collectstatic --no-input
gunicorn --bind 0.0.0.0:8000 backend.wsgi
