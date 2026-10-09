import os
import re

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "local-development-secret")
EMAIL_PATTERN = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
FORM_SUBMIT_URL = "https://formsubmit.co/contatoboradesbugar@gmail.com"


@app.route("/")
def home():
	return render_template("index.html")


@app.route("/obrigado")
def thanks():
	return render_template("thanks.html")


@app.route("/contato", methods=["POST"])
def contact():
	name = request.form.get("nome", "").strip()
	sender_email = request.form.get("email", "").strip()
	message = request.form.get("mensagem", "").strip()

	if not name or not EMAIL_PATTERN.fullmatch(sender_email) or not message:
		flash("Preencha nome, e-mail válido e mensagem.", "error")
		return redirect(url_for("home"))

	return redirect(FORM_SUBMIT_URL, code=307)


if __name__ == "__main__":
	app.run(debug=True)
