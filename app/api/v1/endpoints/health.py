"""
Health Check Endpoint (health.py)
=================================
A lightweight, unprotected HTTP route typically designed for Load Balancers (AWS ELB, NGINX) 
or Container Orchestrators (Kubernetes Liveness Probes) to ping continuously. 
If this endpoint ever returns a 500 or times out, the orchestrator automatically restarts the pod.
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    """Return application health status. (Migrated to API V1)"""
    return {"status": "healthy", "service": "FastAPI Phase-2 App", "version": "v1"}
