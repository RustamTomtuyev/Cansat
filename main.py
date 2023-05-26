from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio
import json

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Real-time Data Updates</title>
        <script type="text/javascript">
            var socket = new WebSocket("ws://localhost:8000/ws");

            socket.onmessage = function(event) {
                var data = JSON.parse(event.data);
                document.getElementById("data").innerText = data.join(", ");
            };
        </script>
    </head>
    <body>
        <div id="data"></div>
    </body>
</html>
"""

connected_websockets = set()
sample_data = []

async def update_data():
    while True:
        sample_data.append(int("<1>".strip("<>")))
        data = json.dumps(sample_data)
        for websocket in connected_websockets:
            await websocket.send_text(data)
        await asyncio.sleep(1)  


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_websockets.add(websocket)

    try:
        while True:
            await websocket.receive_text()
    finally:
        connected_websockets.remove(websocket)

@app.get("/")
def get():
    return HTMLResponse(content=html, status_code=200)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(update_data())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)









# from fastapi import FastAPI, WebSocket
# from data import dataa
# import asyncio
# import json
# app = FastAPI()


# @app.websocket("/")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         # await asyncio.sleep(0.1)
#         # data = await websocket.receive_text()
#         # message = await websocket.receive_text()
#         # print(f"Received message from client: {message}")
        
#         converted = [int(item.strip("<>")) for item in dataa]
#         await websocket.send_text(json.dumps(converted))

        






# from fastapi import FastAPI, WebSocket
# # from data import dataa
# import asyncio
# import json


# app = FastAPI()






# @app.websocket("/")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         await websocket.receive_text()

#         while True:
#             try:
#                 data=await websocket.receive_text()  
#                 print(data)
#             except:
#                 pass


#         print(message)
#         converted = [int(item.strip("<>")) for item in dataa]
#         await websocket.send_text(json.dumps(converted))
#         # for i in dataa:
#         #     await websocket.send_text(str(i))







# import asyncio
# from fastapi import FastAPI, WebSocket

# app = FastAPI()

# # Store connected websocket clients
# connected_clients = set()

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     # Establish websocket connection
#     await websocket.accept()

#     # Add client to connected_clients set
#     connected_clients.add(websocket)

    
#     while True:
#             # Receive message from the client
#         message = await websocket.receive_text()
#         print(f"Received message from client: {message}")

#             # Send message to all connected clients
#         await asyncio.gather(*[client.send_text(message) for client in connected_clients])
    
