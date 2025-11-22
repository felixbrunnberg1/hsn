FROM python:3.8

WORKDIR /code

COPY src/ .
COPY config_example.ini ./config.ini


RUN apt-get update && \
    apt-get install -y iputils-ping && \
    rm -rf /var/lib/apt/lists/*ng

CMD ["python", "./main.py"]