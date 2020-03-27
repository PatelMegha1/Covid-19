FROM python:3.9.0a5-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python ./manage.py runserver