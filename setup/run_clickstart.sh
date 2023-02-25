cd ..
python manage.py shell <<FOO 
exec(open('setup/src/clickstart_prod.py').read())
FOO