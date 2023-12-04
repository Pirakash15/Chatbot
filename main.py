from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from database import ChatDatabase
from manuals import ManualsManager
app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load templates
templates = Jinja2Templates(directory="templates")

# Initialize the database
db = ChatDatabase()
manuals_manager = ManualsManager()

# HTML response for the main page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    messages = db.get_all_messages()
    help_options = manuals_manager.folders_list
    available_pdf_list = manuals_manager.file_urls_dict
    return templates.TemplateResponse("index.html", {"request": request, "help_options": help_options, "pdfs": available_pdf_list, "messages": messages, })

# WebSocket endpoint for chat
@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    with db:
        await websocket.accept()
        try:
            while True:
                user_message = await websocket.receive_text()
                db.insert_message("user", user_message)
                bot_message = "Bot: Received your message - " + user_message
                db.insert_message("bot", bot_message)
                await websocket.send_text(bot_message)
        except WebSocketDisconnect as e:
            print(f"WebSocketDisconnect: {e}")
        finally:
            db.close()

# New route to clear all messages
@app.post("/clear-messages")
async def clear_messages():
    db.clear_messages()
    return {"message": "All messages cleared successfully"}

@app.get("/open-manual/{folder}")
async def open_manual(folder: str):
    manual_path = manuals_manager.get_manual_path(folder)

    if manual_path:
        # You can customize the response, for example, redirect to the manual URL
        return {"message": f"Available manuals at the {folder} folder: {manual_path}"}
    else:
        return {"message": f"No manual found at the {folder} folder"}

