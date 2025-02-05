from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class StartData(BaseModel):
    service_running: str
    user_name: str
    work_item: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

service_state = StartData(service_running="stopped", user_name="", work_item="")


@app.get("/")
async def get_status() -> StartData:
    global service_state
    return service_state


@app.put("/toggle-service")
async def toggle_service(start_data: StartData) -> StartData:
    global service_state

    if service_state.service_running == "stopped":
        service_state = start_data.model_copy()
        service_state.service_running = "running"
        return service_state

    if service_state.service_running == "running":
        service_state.user_name = ""
        service_state.work_item = ""
        service_state.service_running = "stopped"

        return service_state
