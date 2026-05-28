from flask import Flask, request, Response
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
import asyncio
import json

app = Flask(__name__)

# pega do Azure Bot
APP_ID = "41753d4c-12b5-448b-af15-f52ed6da67bc"
APP_PASSWORD = ""

settings = BotFrameworkAdapterSettings(APP_ID, APP_PASSWORD)
adapter = BotFrameworkAdapter(settings)

async def bot_logic(turn_context: TurnContext):
    user_message = turn_context.activity.text.lower()

    responses = {
        "rhel": "O Red Hat Enterprise Linux é uma distribuição Linux corporativa focada em estabilidade e segurança.",
        "fedora": "O Fedora funciona como plataforma de inovação da Red Hat.",
        "azure": "A Azure é a plataforma de computação em nuvem da Microsoft.",
        "cloud": "Cloud Computing é o fornecimento de recursos pela internet.",
        "ia": "IA generativa cria respostas automaticamente usando modelos de linguagem."
    }

    reply = "Desculpe, ainda não sei responder isso."

    for key in responses:
        if key in user_message:
            reply = responses[key]
            break

    await turn_context.send_activity(reply)

@app.route("/")
def home():
    return "Bot online"

@app.route("/api/messages", methods=["POST"])
def messages():
    body = request.json

    activity = Activity().deserialize(body)
    auth_header = request.headers.get("Authorization", "")

    async def aux_func():
        await adapter.process_activity(activity, auth_header, bot_logic)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(aux_func())

    return Response(status=201)

if __name__ == "__main__":
    app.run(debug=True)