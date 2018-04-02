# yellowant-sample-django-app

Sample Django application for creating a Todo List Manager for YellowAnt

## Getting Started

These instructions will get you started with deploying this YellowAnt application under 15 minutes.

### Prerequisites

```
Django v2
python3
```

### Installation

Clone this repo.

Create a new virtual environment for this application and activate it.
[Python 3 Virtual Environment Tutorial](https://docs.python.org/3/tutorial/venv.html)

After activating the virtual environment, point to the root folder of this project and run:
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

## Register this application with your YellowAnt Developer account

1. Once you have logged into YellowAnt, head over to your team's subdomain developer page, <https://your-team-subdomain.yellowant.com/developers/>

2. Click on the button "Create New Application"

3. Fill the form and click "Create Application":
    - Display Name: A human readable display name for the application.
    - Invoke Name: A simple single word which users can use to control this app.
    - Short Description: A human readable short description

4. After the application is created you will be at the application overview page. You need update the application with more information and click on "Update Application".
    - API URL: The endpoint through which YellowAnt will communicate with this app.
    - Installation Website: The URL of your app where users will be able to begin integrating their YellowAnt accounts with this app.
    - Redirect URL: The endpoint at which YellowAnt will send the OAuth codes for user authentication.
    - Icon URL: A URI which points to an icon image for this app.
    - Creator Email: Your Email
    - Privacy Policy URL: Any policy or TOC URL for your app.
    - Documentation URL: A documentation website URL for your app.
    - Is Application Active: set to "Active"
    - Is Application Production or Testing: set to "Production"
    - Application Visibility: set to "Public"

5. You need to create the 5 functions that are understood by this Django app.
    1. createitem(title, description): create a new todo item
        - title [varchar, required]: title of a todo item
        - description [varchar]: extra details of a todo item
    2. getlist(): get a list of todo items
    3. getitem(id): get a single todo item
        - id [int, required]: id of the todo item
    4. updateitem(id, title, description): update a todo item
        - id [int, required]: id of the todo item
        - title [varchar]: new title of the todo item
        - description [varchar]: new description for the todo item
    5. deleteitem(id: int): delete a todo item
        - id [int, required]: id of the todo item
  
## Update variables and settings in the Django App

6. Open up the file `yellowant_todoapp/settings.py`

7. Update the variables `YA_REDIRECT_URL`, `YA_APP_ID`, `YA_CLIENT_ID`, `YA_CLIENT_SECRET`, `YA_VERIFICATION_TOKEN` from the application overview page:
    - YA_REDIRECT_URL: The `Redirect URL`
    - YA_APP_ID: The integer `ID`
    - YA_CLIENT_ID: The `Client ID`
    - YA_CLIENT_SECRET: The `Client Secret`
    - YA_VERIFICATION_TOKEN: The `Verification Token`

## Run the Django application server
`python manage.py runserver`