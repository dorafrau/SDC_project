# Basierend auf einem offiziellen Python-Image
FROM python:3.8-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Datei requirements.txt zuerst, um den Cache besser nutzen zu können
COPY ./requirements.txt /app/requirements.txt

# Installiere alle benötigten Pakete aus der requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den restlichen Quellcode der Anwendung in das Arbeitsverzeichnis
COPY ./ /app/

# Streamlit-spezifische Konfiguration
EXPOSE 8501

# Führe die Streamlit-App aus
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
