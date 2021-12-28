cd ..
python manage.py shell <<FOO
exec(open('setup/create_db.py').read())
FOO
