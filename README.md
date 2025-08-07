- For every new project in Django

## Project Setup
---


1. Create a folder for the project 
    - Open the folder in IDE (VS Code)

2. Open terminal in the VS Code.

3. Create a new virtual environment for the project
    - `python -m venv <virtual_env_name>`
    - Eg:, `python -m venv virt`

    - This will generate a new folder by the name specified.

4. Activate the virtual environment.
    - Inside the virtual environment folder, here, `virt`, there will be a folder called `Scripts` and an `activate` script will be present inside. This helps us **activate** the virtual environment.
        - To activate, run `virt/Scripts/activate`
    - Please note that in UNIX based systems like MacOS and Linux, the activate script will be inside the `bin` subfolder. 
        - In these systems, we have to run `source virt/bin/activate`.

    - *Once Activated, in most systems, the shell prompt will show the virtual environment name.*

5. Create a file called `.gitignore` inside the project folder.
    -   This file lists out the folders and files to be skipped from being tracked by git.
    - This includes the virtual environment folder, the database file for sql lite, media folder, credentials files, etc...
    - Eg:
        ```bash
        # .gitignore
        virt/
        media/
        db.sqlite3
        credentials.txt
        __pycache__/
        ```

6. Installations - Do the necessary installations
    - Django
        - `pip install django`
    - Pillow - to support ImageField in django. 
        - `pip install pillow`
    
7. Freeze the requirements for the project (dependencies)
    - `pip freeze > requirements.txt`
    - This creates a file called `requirements.txt` listing all libraries, packages, etc and their installed versions.
    - Re run this command every time new libaries or packages are installed.
    - This file is crucial in setup of the project later on in a different system or on the server.

## Initializing the Django Project 

- Ensure the virtual environment is activated.

- Start the django project
- `django-admin startproject <projectName>`
    - Eg : `django-admin startproject yshop`
- **Do not use spaces in project naming.**

- New django project folder is generated on executing the above command.
- Folder structure generated : 
    ```
    project-folder - 
                    |- virt/
                    |- .gitignore
                    |- requirements.txt
                    |- ReadMe.md
                    |
                    |
                    |- vshop -|
                            |- manage.py
                            |- vshop
    ```
- As you might have noticed, there is a django project folder named `vshop` and a subfolder by the same name.
- The outer vshop folder is called the `django project folder`
    - This contains every relevant files related to the django project.
- The inner `vshop` folder is called the `django project root folder`
    - This contains mainly the configuration files for the django server.


## Now the project is setup and initialized.
- Please note
    -   Every time we start working on the project, we just need to activate the virtual environment.
    - Other steps are only for first time setup.
---

# Test the server
## Migrate the schema to DB
- By default, django framework uses an SQL Lite database.
- Ensure you are inside the created **django project folder**.
    - `cd vshop`
- Run `python manage.py migrate` to migrate the schema
- Run `python manage.py runserver`
- In the terminal output, a link will appear for the development server like `127.0.0.1:3000/`
    - Ctrl + click on the link to open the browser and see the test page.

    - Go back to the terminal and do `Ctrl + C` to close the server.

# Django Admin panel
- An admin panel comes pre-built in django installation.
- This helps in easy administration of the website by giving us control through CRUD operations and much more of the models registered with it.
- Let's create the credentials for accessing admin panel.
- Run the following command and follow the instructions that follow 
    - `python manage.py createsuperuser`
    - Super user is the term for user with admin privileges.
- Now run the server like earlier
- Go to the link 
- In the browser, type `/admin` to the end of the url.
    - Eg: `127.0.0.1:3000/admin`
    - This opens the admin panel
    - Type the credentials we created.


---
# Django Apps

- Apps are re-usable blocks of the project.
- We divide our django project into different apps to separate the logic for handling different features or set of features. 
- This enables the re-usability of these apps in other projects.

- Let's create our first app

## Initializing a new app

- Let's call our first app as `mainapp`.
- Quit the server if it is running

### To create the new app,

- cd into the django project folder if you are not already there.

- `cd vshop`
- Now on doing `ls` you will be able to see a file called `manage.py`

- `manage.py` is a shortcut to the django-admin.
    - major management tasks for the django project will be handled through this python script.

## 1. Create app - initialize a new app
- `python manage.py startapp <app_name>`
- Eg: `python manage.py startapp mainapp`
- *Please take care to ensure that no other inbuilt apps or packages exist of the same name.*

## 2. Create app specific `urls.py`
- This practice helps us handle the urlpatterns in a more divided fashion.
- Create a new `urls.py` file inside the app folder.

- **Including this URLconf in the project urls.py**
    - In the project `urls.py` inside the project root folder,
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    For example, now our project urls.py becomes:










