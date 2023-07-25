# RestaurantAPI

# Create virtual Environment using venv instead of pipenv which did not work with my machine 😴

python -m venv _myenv

# Activate it

source _myenv/Scripts/activate

# Then the following commands

python manage.py makemigrations 

python manage.py migrate

python manage.py runserver




