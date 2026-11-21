from flask import Flask, jsonify, redirect

app = Flask(__name__)

@app.route("/")
def accueil():
	return 'Bonjour! <a href="/aller">Cliquez ici</a>'

@app.route("/aller")
def aller():
	return redirect("/page2")

@app.route("/page2")
def page2():
	return 'Vous avez ete redirigee vers 2 <a href="/">Retour</a>'

@app.route("/api")
def api():
	return jsonify(message="salam aleykum", statut="ok")

if __name__ == "__main__":
	app.run(host="0.0.0.0" , port=5000)
EOF
