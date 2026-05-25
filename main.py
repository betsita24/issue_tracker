from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timing_middleware_p
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()

app.middleware("http")(timing_middleware_p)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(issues_router)