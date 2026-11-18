from fastapi import FastAPI

app = FastAPI(
    title="SkillPath API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to SkillPath API"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }