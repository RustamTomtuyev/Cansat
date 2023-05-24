


from fastapi import FastAPI, WebSocket
from data import dataa
import asyncio
import json
app = FastAPI()


@app.websocket("/api/data")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # await asyncio.sleep(0.1)
        # data = await websocket.receive_text()
        converted = [int(item.strip("<>")) for item in dataa]
        await websocket.send_text(json.dumps(converted))
        # for i in dataa:
        #     await websocket.send_text(str(i))
