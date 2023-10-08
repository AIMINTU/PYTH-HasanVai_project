#django application
1.django install:
==>pip install django
2.create a dajango project:
==>django-admin startproject projectName
change directory:
==> cd . \bms\
create a app in the bms project:
==>py .\manage.py startapp bookms
Run the django server:
==>py manage.py runserver
crete a folder on the bookms:
==>templates and take one html file on the templates.
we would like to take class on the bookms folder.
crete Migrations:
py manage.py makemigrations
data base a migration ke migrate korar janno command hollo:
open the dp.sqlite3 then ==>python manage.py migrate
add another html page 
==>go to the templates and make the html page.
http verbs:
1. Retrieve a single item (GET)
2. Retrieve a list of items (GET)
3. Create an item (POST)
4. Update an item (PUT)
5. Delete an item (DELETE)
