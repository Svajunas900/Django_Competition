FROM python:3.10-slim

WORKDIR /python_fastapi

COPY requirements.txt /python_fastapi/

RUN pip install -r requirements.txt

RUN pip install "fastapi[standard]"

COPY . /python_fastapi

CMD [  "fastapi", "run", "main.py", "--port", "7000" ]

EXPOSE 7000