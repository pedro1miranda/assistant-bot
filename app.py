from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():

    return """
    
    <h1>RHEL Assistant Bot</h1>

    <p>Chatbot funcionando!</p>

    <p>Projeto de Computação em Nuvem</p>

    """

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message", "").lower()

    responses = {

        "rhel": "O Red Hat Enterprise Linux é uma distribuição Linux corporativa focada em estabilidade e segurança.",

        "fedora": "O Fedora funciona como plataforma de inovação da Red Hat.",

        "azure": "A Azure é a plataforma de computação em nuvem da Microsoft.",

        "cloud": "Cloud Computing é o fornecimento de recursos computacionais pela internet.",

        "ia": "IA generativa utiliza modelos capazes de gerar respostas automaticamente."
    }

    for key in responses:

        if key in user_message:

            return jsonify({
                "response": responses[key]
            })

    return jsonify({
        "response": "Desculpe, ainda não sei responder isso."
    })

if __name__ == "__main__":

    app.run(debug=True)