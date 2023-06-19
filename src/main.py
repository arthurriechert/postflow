from cli import cli
import blogger
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import os
from typing import Optional
from enum import Enum
from stream import ConnectionManager 
from starlette.websockets import WebSocketDisconnect

app = FastAPI()
manager = ConnectionManager()

origins = [
    "http://localhost:5173",  # Replace with the origin of your frontend app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Tools(str, Enum):
    blogger = "blogger"

@app.get("/api/tools/blogger/gpt-4")
async def openai_blog_update():
    await blogger.run_single_update(manager)
    await manager.broadcast("Starting")
    return {"status": "Update process started"}

@app.get("/api/tools/chat/gpt-4")
async def openai_chat_completion():
    return {"status": "Chat sent"}

@app.get("/api/test")
async def get_test_data() -> dict:
    return {"func": "test", "message": '<h2>this is a test</h2>\n<p style="margin-top: -15px">I hope the test was successful</p>'}

@app.websocket("/api/status/stream")
async def stream_status(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A client has disconnected")

@app.get("/message/{message}")
async def send_message(message: str):
    await manager.broadcast(message)
    return {"message", "Message sent"}

if __name__ == "__main__":

    blogger.run_single_update() 

    cli()
