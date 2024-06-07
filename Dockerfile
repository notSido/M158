FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app
COPY ./main.py /app/main.py
COPY ./wait-for-it.sh /app/wait-for-it.sh

CMD ["./wait-for-it.sh", "db:3306", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
