from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/missao")
def missao():
    return render_template("missao.html")

@app.route("/missao1")
def missao1():
    return render_template("missao1.html")

@app.route("/confirmacao", methods=["POST"])
def confirmacao():
    dia = request.form.get("dia")
    horario = request.form.get("horario")

    with open("respostas.txt", "a") as arquivo:
        arquivo.write(f"Dia: {dia} | Horário: {horario}\n")

    return redirect(url_for("aceita"))

@app.route("/aceita")
def aceita():
    return render_template("aceita.html")

@app.route("/decisao", methods=["POST"])
def decisao():
    resposta = request.form.get("resposta")

    with open("respostas.txt", "a") as arquivo:
        arquivo.write(f"Resposta final: {resposta}\n")

    return redirect(url_for("final"))

@app.route("/final")
def final():
    return render_template("final.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)