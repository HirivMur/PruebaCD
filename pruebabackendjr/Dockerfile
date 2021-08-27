# Use an official Python runtime as a parent image
FROM python:3.7

#set directoty where CMD will execute
WORKDIR /usr/src/viri

COPY . /usr/src/viri

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate

# Run app.py when the container launches
CMD exec gunicorn pruebabackendjr.wsgi:application --bind 0.0.0.0:8000 --workers 1