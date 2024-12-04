FROM python:3.10.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
#PORT
EXPOSE 5050

ENV PYTHONUNBUFFERED 1

CMD ["python", "toxic_check_service.py"]
