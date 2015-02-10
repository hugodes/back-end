# back-end
Back-end of the project

##Install...

Install imagemagic for you distribution:
Example: yum install imagemagic

pip install -r requirements.pip

##... & Launch

cd back_end
./manage.py migrate
./manage.py runserver
go to http://127.0.0.1:8000/

##Using the admin

cd back_end
./manage.py createsuperuser
./manage.py runserver
go to http://127.0.0.1:8000/admin

## Retrieving JSON

### From a shelf name:

http://127.0.0.1:8000/get_json/<shelf_name>/

### From a search:

http://127.0.0.1:8000/get_json/search/?q=<arg1>&q=<arg2>&....



