from collections import defaultdict
from typing import List

from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"],
)

API_KEY = "ak_6vp0jhlhwg8uf93qyixrnyf5"
EMAIL = "24f2006261@ds.study.iitm.ac.in"


class Event(BaseModel):
    user: str
    amount: float
    ts: int


class AnalyticsRequest(BaseModel):
    events: List[Event]


@app.post("/analytics")
async def analytics(body: AnalyticsRequest, x_api_key: str = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

    events = body.events
    total_events = len(events)
    unique_users = len({e.user for e in events})

    revenue = 0.0
    per_user_positive = defaultdict(float)
    for e in events:
        if e.amount > 0:
            revenue += e.amount
            per_user_positive[e.user] += e.amount

    top_user = None
    if per_user_positive:
        top_user = max(per_user_positive.items(), key=lambda kv: kv[1])[0]

    return {
        "email": EMAIL,
        "total_events": total_events,
        "unique_users": unique_users,
        "revenue": revenue,
        "top_user": top_user,
    }


@app.get("/")
async def root():
    return {"status": "ok"}from collections import defaultdict
from typing import List

from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"],
)

API_KEY = "ak_6vp0jhlhwg8uf93qyixrnyf5"
EMAIL = "24f2006261@ds.study.iitm.ac.in"


class Event(BaseModel):
    user: str
    amount: float
    ts: int


class AnalyticsRequest(BaseModel):
    events: List[Event]


@app.post("/analytics")
async def analytics(body: AnalyticsRequest, x_api_key: str = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

    events = body.events
    total_events = len(events)
    unique_users = len({e.user for e in events})

    revenue = 0.0
    per_user_positive = defaultdict(float)
    for e in events:
        if e.amount > 0:
            revenue += e.amount
            per_user_positive[e.user] += e.amount

    top_user = None
    if per_user_positive:
        top_user = max(per_user_positive.items(), key=lambda kv: kv[1])[0]

    return {
        "email": EMAIL,
        "total_events": total_events,
        "unique_users": unique_users,
        "revenue": revenue,
        "top_user": top_user,
    }


@app.get("/")
async def root():
    return {"status": "ok"}
