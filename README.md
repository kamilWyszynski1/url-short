# url-short
Technical task's project. Simple Web App that shorten user's Url

## Desing
1. User insert his url in input and press submit button.
2. App checks whether shortcut for that url exists. 
3. App either shows data which already exist or create that data and shows it after that.


## Used technologies:
* [Django](https://docs.djangoproject.com/en/2.2/) - Backend
* [Django-Rest-Framework](https://www.django-rest-framework.org/) - Api
* [AgnularJs](https://angularjs.org/) - Front-end

## Running the Project locally
First, clone the repository to your local machine:
```
  git clone git@github.com:kamilWyszynski1/url-short.git
```
Setup virtaul environment:
```
  virtualenv env
```
Activate virtual environment:
```
  source env/bin/activate
```

Install the requirements:
```
  pip install -r requirements.txt
```

Create the database:
```
python manage.py migrate
```
Finally, run the development server:
```
python manage.py runserver
```
The project will be available at **127.0.0.1:8000**
