# umcu_proj
I used vagrant, virtualenv and Django to tackle this project. I decided to try something new with this project, so this is 
the first time I've ever attempted to use Django. There are some features that I wasn't able to complete unfortunately. 

I've included a requirements file with Django and packages you might need.
pip install -r requirements.txt

Django has an interesting SQL interface.
Navigate to the umcu folder, which should have manage.py located in it.
To set up the database:

python manage.py makemigrations
python manage.py migrate

Then, run:
python manage.py runserver 0.0.0.0:PORT
where PORT can be specified by you. I chose 8000 because that's how my vagrant machine ports are set up.

It should display something like:
Performing system checks...

System check identified no issues (0 silenced).
June 02, 2016 - 10:02:22
Django version 1.9.6, using settings 'umcu.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.

Go to the address listed above, and add '/memberinfo/new_form' to get to the actual form (http://localhost:8000/memberinfo/new_form in my case)
Sorry for the usability flaw here, I know it's a problem you can't just click to the form. Going to /memberinfo gives you a blank page with a link though!

TODO:
	Javascript filtering so the user doesn't have to hit "submit" to realize he has a ton of errors
	An actual home page
	Some CSS sprucing
	Custom filtering (Get rid of special characters, more specific password limitations)






