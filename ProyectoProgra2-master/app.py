from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/index_admi")
def index_admi():
    return render_template("index_admi.html")

@app.route("/index_cliente")
def index_cliente():
    return render_template("index_cliente.html")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/perfilCliente")
def perfilCliente():
    return render_template("perfilCliente.html")

@app.route("/register")
def register():
    return render_template("register.html")
    
@app.route("/reservacion")
def reservacion():
    return render_template("reservacion.html")

@app.route("/reservaciones_admi")
def reservaciones_admi():
    return render_template("reservaciones_admi.html")

@app.route("/servicios_admi")
def servicios_admi():
    return render_template("servicios_admi.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/tablareservaciones")
def tablareservaciones():
    return render_template("tablareservaciones.html")

@app.route("/tablasreservaciones_admi")
def tablasreservaciones_admi():
    return render_template("tablasreservaciones_admi.html")

if __name__ == "__main__":
    app.run(debug=True)
