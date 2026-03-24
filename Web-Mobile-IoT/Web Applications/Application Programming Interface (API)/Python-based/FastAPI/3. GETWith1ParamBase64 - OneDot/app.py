from fastapi import FastAPI
import base64
import io
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, Base64Code: str):
    item = {"item_id": item_id, "Base64Code": Base64Code}
    i = base64.b64decode(Base64Code)
    i = io.BytesIO(i)
    i = mpimg.imread(i, format='JPG')
    plt.imshow(i, interpolation='nearest')
    plt.show()
    return item