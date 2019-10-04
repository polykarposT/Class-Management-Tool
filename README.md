# Class-Management-Tool
Class Management Tool (CMT) is a web app for teachers and education professionals to help them organize their Classes and keep a record of students and their progress.

You can download and try it with the following credentials:
 
 username: test
 password: test

To create an account of your choice and use the web app with empty database reseting primary keys from start yo have to do the following steps:

1) Delete db.sqlite3 and every file in migrations folder except __init__.py file
2) Open a terminal/cmd in project directory(/classs) and run the command python manage.py makemigrations
3) Run the command python manage.py migrate
4) To set the account of your choice run the command python manage.py createuseruser and follow the steps.
