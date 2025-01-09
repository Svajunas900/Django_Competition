FROM python:3.10-slim

WORKDIR /python_fastapi

COPY requirements.txt /python_fastapi/

RUN pip install -r requirements.txt

COPY . /python_fastapi

CMD [ "python" "main.py" ]

EXPOSE 7000