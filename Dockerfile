FROM python:3.9-alpine

WORKDIR /app

COPY . /app

RUN chmod +x app.py

RUN pip install flask pyyaml


CMD ["python", "app.py"]