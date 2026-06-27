from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()


@app.get("/")
def home():
    return {"status": "SMB AI Receptionist is running."}


@app.post("/sms")
async def sms_reply(request: Request):
    form_data = await request.form()
    incoming_msg = form_data.get("Body", "")
    response = MessagingResponse()
    response.message(f"You said: {incoming_msg}")
    return PlainTextResponse(content=str(response), media_type="application/xml")