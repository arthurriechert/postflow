from cli import cli
import blogger
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import os
from typing import Optional
from enum import Enum
from stream import ConnectionManager 
from starlette.websockets import WebSocketDisconnect

# Set up FastAPI
app = FastAPI()
manager = ConnectionManager()

# Only allow local client while testing
origins = [
    "http://localhost:5173",
]

# Setup CORS    
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Tools(str, Enum):
    """
    Used to check for appropriate tool when someone calls API

    """
    blogger = "blogger"

@app.get("/api/tools/blogger/gpt-4")
async def openai_blog_update():
    """
    Attempts the process of generating a new blog post

    Args:
        None

    Returns:
        (dict): Status message

    """
    await blogger.run_single_update(manager)
    await manager.broadcast("Starting")
    return {"status": "Update process started"}

@app.get("/api/tools/chat/gpt-4")
async def openai_chat_completion():
    """
    Gets chat completion based on chat history

    * Note: Takes json body

    Args:
        None

    Returns:
        (dict): Status message

    """
    return {"status": "Chat sent"}

# CONSIDER REVISING THIS METHOD OF TRANSMITTING STATUSES
@app.websocket("/api/status/stream")
async def stream_status(websocket: WebSocket):
    """
    Transmits messages across websocket API to Client

    Args:
        websocket (WebSocket): Interface for using web sockets

    Returns:
        None
    
    """

    # Connect to the websocket manager
    await manager.connect(websocket)

    # Broadcast messages
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A client has disconnected")

@app.get("/api/test/{message}")
async def send_message(message: str):
    """
    Sends a test message over the websocket stream

    Args:
        message (str): The message you want to transmit

    Returns:
        (dict): A status message

    """

    # Send the message over websocket
    await manager.broadcast(message)
    
    return {"status": "Message sent"}

if __name__ == "__main__":
    """
    Run the CLI

    """

    # Starts the command line interface
    cli()
