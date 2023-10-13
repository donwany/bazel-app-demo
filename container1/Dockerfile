FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 1957

CMD ["uvicorn", "app1:app", "--host", "0.0.0.0", "--port", "1957"]
