from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CloudOps Ticket Analyzer")


class Ticket(BaseModel):
    title: str
    description: str
    severity: str


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "cloudops-ticket-analyzer"
    }


@app.post("/analyze")
def analyze_ticket(ticket: Ticket):
    risk_score = 0

    if ticket.severity.lower() == "critical":
        risk_score += 70
    elif ticket.severity.lower() == "high":
        risk_score += 50
    elif ticket.severity.lower() == "medium":
        risk_score += 30
    else:
        risk_score += 10

    keywords = ["outage", "breach", "failed", "unauthorized", "latency"]

    for word in keywords:
        if word in ticket.description.lower():
            risk_score += 5

    recommendation = "Escalate immediately" if risk_score >= 70 else "Monitor and troubleshoot"

    return {
        "title": ticket.title,
        "severity": ticket.severity,
        "risk_score": risk_score,
        "recommendation": recommendation
    }
