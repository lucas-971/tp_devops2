FROM python:3.6

WORKDIR /tp_devops

COPY . .

RUN pip install -r requirements.txt



CMD ["python", "app.py"]
