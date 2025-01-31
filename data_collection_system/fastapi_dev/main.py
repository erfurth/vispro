from fastapi import FastAPI


app = FastAPI()


@app.get("/grafana-test")
async def grafana_test() -> dict:
    return {"user_name": "Dagobert Duck", "work_item": "Glückstaler"}
