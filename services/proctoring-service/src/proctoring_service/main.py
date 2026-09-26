from fastapi import FastAPI

app = FastAPI(title="proctoring-service", version="0.1.0")


@app.get("/health", tags=["system"])
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "proctoring-service"}
