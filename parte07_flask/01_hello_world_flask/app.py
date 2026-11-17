from flask import Flask

# ativar o framenwork
app = Flask(__name__)

# criar uma rota para o conteúdo
@app.route("/")
def hello_world():
    return "Olá, mundo! 🌍👋"

#executar a aplicação
if __name__== "__main__":
    app.run(debug=True)