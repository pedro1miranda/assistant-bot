from flask import Flask, request, jsonify

app = Flask(__name__)  # <- ISSO TEM QUE SER A PRIMEIRA COISA

@app.route("/")
def home():
    return "OK"

@app.route("/api/messages", methods=["POST"])
def messages():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "type": "message",
            "text": "Erro: requisição inválida."
        })

    user_message = data.get("text", "").lower()

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

    return jsonify({
        "type": "message",
        "text": reply
    })

if __name__ == "__main__":
    app.run(debug=True)