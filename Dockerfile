FROM python:3.11.8


ENV TZ Asia/Shanghai

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD [ "python", "main.py" ]