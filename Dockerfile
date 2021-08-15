FROM python:3.9.6-slim-buster
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR  /app
COPY . .
ENTRYPOINT ["supervisord", "-n" ]
