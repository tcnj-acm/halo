cd ..
python manage.py shell <<FOO
exec(open('setup/src/create_db.py').read())
FOO
