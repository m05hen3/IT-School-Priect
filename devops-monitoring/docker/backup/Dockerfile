FROM python:3.11-alpine

WORKDIR /app

COPY scripts/backup.py /app/backup.py
COPY docker/backup/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENV BACKUP_INTERVAL=5
ENV BACKUP_DIR=/backup

RUN mkdir -p /backup

CMD ["python3", "backup.py"]