FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download en_core_web_sm

ENV WANDB_API_KEY="39fbd2c790b8bcf1bcb7a993e0ad9b8f4740c019"

COPY . /app/

EXPOSE 5000

CMD ["python", "app.py"]
