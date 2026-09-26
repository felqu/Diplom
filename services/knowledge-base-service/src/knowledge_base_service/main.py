from fastapi import FastAPI

app = FastAPI(title="knowledge-base-service", version="0.1.0")


@app.get("/health", tags=["system"])
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "knowledge-base-service"}
