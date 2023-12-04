from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load templates
templates = Jinja2Templates(directory="templates")

# Sample list of folders or options
help_options = ["F1", "F2", "F3", "F4"]

# HTML response for the main page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "help_options": help_options})

# WebSocket endpoint for chat
@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        user_message = await websocket.receive_text()
        # Implement your chatbot logic here
        bot_message = "Bot: Received your message - " + user_message
        await websocket.send_text(bot_message)


