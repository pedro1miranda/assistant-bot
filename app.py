from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "OK - Bot Online"

@app.route("/api/messages", methods=["POST"])
def messages():
    # pega JSON de forma segura (Azure Bot às vezes manda payload diferente)
    data = request.get_json(silent=True)

    print("DEBUG - payload recebido:", data)

    # proteção caso venha vazio ou inesperado
    if not data:
        return jsonify({
            "type": "message",
            "text": "Erro: requisição inválida (sem payload)."
        })

    # Azure Bot normalmente envia "text"
    user_message = data.get("text")

    if not user_message:
        return jsonify({
            "type": "message",
            "text": "Erro: mensagem vazia recebida."
        })

    user_message = user_message.lower()

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

    print("DEBUG - resposta enviada:", reply)

    return jsonify({
        "type": "message",
        "text": reply
    })

if __name__ == "__main__":
    app.run(debug=True)