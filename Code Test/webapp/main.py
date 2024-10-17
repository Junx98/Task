#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import necessary packages
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[dict] = [] #create an empty list that store the connections. Each connection is a dictionary to the username and websocket

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        
        # The first message is expected to be username
        try:
            username = await asyncio.wait_for(websocket.receive_text(), timeout=30) #A time limit is set for entering the username
            
        #If the user does not enter the username within given time, an error will be raised and the connection will be closed
        except asyncio.TimeoutError:
            await websocket.close()
            return None

        connection = {"username": username, "websocket": websocket}
        self.active_connections.append(connection) #Store the connection
        await self.broadcast(f"{username} has joined the chat!")
        return connection

    def disconnect(self, connection: dict):
        self.active_connections.remove(connection)

    async def broadcast(self, message: str):
        #create a list that store the connection which the client has disconnected
        disconnected_connections = []

        #iterate through the active connection list and attempts to send message to each connection
        for connection in self.active_connections:
            try:
                await connection["websocket"].send_text(message)
            except:
                #if fail to send message, add that connction to disconnected_connection, and disconnect them.
                disconnected_connections.append(connection) 
        for connection in disconnected_connections:
            self.disconnect(connection)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    #establish connection using ConnectionManager
    connection = await manager.connect(websocket)

    #if no connection, terminated the function
    if connection is None:
        return

    #store username for later use
    username = connection["username"]
    try:
        while True:
            data = await websocket.receive_text() #store the content of a message
            message = f"{username}: {data}" #format the message as instructed
            await manager.broadcast(message)
    except WebSocketDisconnect:
        manager.disconnect(connection)
        await manager.broadcast(f"{username} has left the chat.")
    


# In[ ]:




