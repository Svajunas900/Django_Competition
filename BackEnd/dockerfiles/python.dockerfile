FROM python:3.10

WORKDIR /django_app

COPY requirements.txt /django_app/

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000