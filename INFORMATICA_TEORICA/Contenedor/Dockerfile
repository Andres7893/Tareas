FROM python:3.9-slim
WORKDIR /app
COPY contenedor2.py .
RUN pip install fastapi uvicorn requests
CMD ["uvicorn", "contenedor2:app", "--host", "0.0.0.0", "--port", "5000"]