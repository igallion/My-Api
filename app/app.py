from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/get-message")
async def read_root():
    return {"Message": f"Hello from {str(socket.gethostname())}"}