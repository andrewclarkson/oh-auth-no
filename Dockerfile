FROM python:3

WORKDIR /usr/share/app

# Add the requirements file to the container
COPY requirements.txt ./

# Install the python packages
RUN pip install -r requirements.txt

# Open up port 8000 for other container's only
EXPOSE 8000

CMD gunicorn --reload -b 0.0.0.0:8000 app:app
