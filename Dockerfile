FROM python:3.10

WORKDIR /app

# Копируем зависимости из backend
COPY backend/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь backend внутрь контейнера
COPY backend/ .

# Запускаем FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
