# Commands to work with

----
## installing django
> pip install django

----
## checking the status of installation 
> python -m django --version

----
## creating django project
> django-admin startproject proj1

----
## opening the workspace in the VS Code editor
code .

----
## Verify the status of project creation by running the local server
1. go into the folder where manage.py file is located, by using cd command 
    eg: cd proj1
2. Type below command in the command prompt
    > python manage.py runserver

#### will receive a message as below
> Watching for file changes with StatReloader
> Performing system checks...
> 
> System check identified no issues (0 silenced).
> 
> You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
> Run 'python manage.py migrate' to apply them.
> Month Date, Year - HH:MM:SS
> Django version 3.0.6, using settings 'proj1.settings'
> Starting development server at http://127.0.0.1:8000/
> Quit the server with CTRL-BREAK.

#### open any web browser and type the below url
http://127.0.0.1:8000/


----
## Creating an app

> python manage.py startapp web

----
## Add web app in the list of INSTALLED_APPS (line 33)

```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web', # add web app to the installed apps
]
```
----
## creating a view ( home page )

1. Go to the views.py in the web folder
2. create a function 


```python

def home(request):
    return render(request,'home.html')
```

3. Go to urls.py file in proj1 folder
4. import home function in the urls.py file

```python
from web.views import home
```

5. update the urlpatterns list with path('home/',home), as below

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home), # update home url
]
```

6. We need to inform the django about the location of html files. The folder we call it as Templates
7. Go to settings.py file and update TEMPLATES : DIR key to :--> os.path.join(BASE_DIR,'templates')

Eg:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

8. Create templates folder in the main project folder i.e., the folder should be along with manage.py file

9. Create home.html file inside templates folder

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    <title>Skill Disk : Django Webinar</title>
</head>
<body>
    <h1 class="amber-text center">Skill Disk</h1>
    <h3 class="purple-text center">Welcome to the webinar on <br> <b>Django : Python web framework</b></h3>
</body>
</html>
```

10.   Check whether all files are saved.

11.   go to command propmt, execute the below command

> python manage.py runserver

12.   IF no error, go to browser and type this url

http://127.0.0.1:8000/home
