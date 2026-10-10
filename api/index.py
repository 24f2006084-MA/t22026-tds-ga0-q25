from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)


TELEMETRY_DATA = json.loads(
[
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 167.29,
    "uptime_pct": 98.793,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 178.79,
    "uptime_pct": 97.29,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 182.41,
    "uptime_pct": 99.252,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 192.01,
    "uptime_pct": 97.495,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 140.8,
    "uptime_pct": 98.384,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 118.66,
    "uptime_pct": 97.848,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 211.35,
    "uptime_pct": 99.025,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 172.91,
    "uptime_pct": 97.706,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 129.05,
    "uptime_pct": 98.182,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 142.5,
    "uptime_pct": 97.292,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 135.18,
    "uptime_pct": 97.802,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 201.22,
    "uptime_pct": 97.8,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 118.88,
    "uptime_pct": 99.226,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 129.2,
    "uptime_pct": 97.185,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 128.57,
    "uptime_pct": 98.627,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 217.63,
    "uptime_pct": 97.408,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 197.16,
    "uptime_pct": 97.836,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 143.19,
    "uptime_pct": 98.099,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 164.32,
    "uptime_pct": 98.847,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 196.1,
    "uptime_pct": 97.85,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 233.53,
    "uptime_pct": 97.315,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 129.21,
    "uptime_pct": 97.457,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 121.41,
    "uptime_pct": 98.607,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 173.23,
    "uptime_pct": 98.348,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 229.45,
    "uptime_pct": 97.456,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 127.36,
    "uptime_pct": 98.894,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 221,
    "uptime_pct": 97.463,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 154.38,
    "uptime_pct": 97.133,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 191.3,
    "uptime_pct": 97.207,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 167.06,
    "uptime_pct": 98.755,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 145.76,
    "uptime_pct": 98.781,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 176.02,
    "uptime_pct": 99.215,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 110.8,
    "uptime_pct": 99.252,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 154.4,
    "uptime_pct": 99.14,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 167.43,
    "uptime_pct": 98.347,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 114.93,
    "uptime_pct": 97.998,
    "timestamp": 20250312
  }

])

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}