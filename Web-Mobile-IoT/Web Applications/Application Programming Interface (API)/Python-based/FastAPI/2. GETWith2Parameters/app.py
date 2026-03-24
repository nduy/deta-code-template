from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id2}")
async def read_user_item(item_id2: str, needy1: str, needy2: str):
    item = {"item_id": item_id2, "needy1": needy1, "needy2": needy2}
    return item