FROM python:3.6

WORKDIR /app

COPY downstream_app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "downstream_app.py"]

