FROM python:3.11-slim

WORKDIR /app

COPY overs .

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "overs.wsgi:application", "--bind", "0:8000"]