FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /urlshortner

COPY . /urlshortner/

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]