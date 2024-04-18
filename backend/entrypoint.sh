python manage.py migrate --no-input
python manage.py loaddata fixture.json
python manage.py load_ingredients
python manage.py collectstatic --no-input
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@foodgram.com', 'Foodgram1')" | python manage.py shell
gunicorn --bind 0.0.0.0:8000 backend.wsgi
