from fastapi import FastAPI
from pydantic import BaseModel
import psutil

app = FastAPI(title="MLOps System Monitor API", version="1.0.0")

# =====================================================================
# LINE-TO-LINE MATCHING: Pydantic Models (Security Guards) 🛡️
# =====================================================================
class HealthMetrics(BaseModel):
    cpu_percent: float
    ram_percent: float

class SystemStatusResponse(BaseModel):
    status: str
    system_health: HealthMetrics

# =====================================================================
# ENDPOINTS (Web Routes) 🌐
# =====================================================================

@app.get("/", tags=["General"])
def home():
    return {"message": "Welcome Master! Use /metrics URL to see live validated system health."}

@app.get("/metrics", response_model=SystemStatusResponse, tags=["Monitoring"])
def get_system_metrics():
    # 1. Hardware se data nikala (Variables ke naam: cpu_usage, ram_usage)
    cpu_usage = psutil.cpu_percent(interval=None)
    ram_usage = psutil.virtual_memory().percent
    
    # 2. Return karte waqt models ki KEYS (cpu_percent, ram_percent) se match kiya!
    return {
        "status": "success",
        "system_health": {
            "cpu_percent": cpu_usage,
            "ram_percent": ram_usage
        }
    }