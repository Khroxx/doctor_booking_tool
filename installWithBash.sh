# LINUX and MAC
#!/bin/bash

# Wechseln in das Projekt
cd doctor_booking_tool/

# create virtual environment
python3 -m venv env

# activate virtual environment
echo "Entering virtual environment"
source env/bin/activate

# install requirements
echo "Installing all requirements"
pip install -r requirements.txt

# database migrations
echo "migrating"
python manage.py makemigrations
python manage.py migrate

echo "Installation complete. Starting Server now"

# start server
python manage.py runserver