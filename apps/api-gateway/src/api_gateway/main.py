from fastapi import FastAPI

app = FastAPI(
    title="Learning Platform API Gateway",
    version="0.1.0",
    description="Единая внешняя точка входа в сервисы платформы.",
)


@app.get("/health", tags=["system"])
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "api-gateway"}
