release: python3 manage.py migrate
web: gunicorn library_xpto.wsgi --timeout 60 --keep-alive 5 --log-level debug --preload --log-file -