FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install --no-cache-dir fastapi "uvicorn[standard]"
COPY src ./src
CMD ["uvicorn", "notification_service.main:app", "--app-dir", "src", "--host", "0.0.0.0", "--port", "8000"]
