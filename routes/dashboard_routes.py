from flask import Flask, render_template, redirect, request, url_for, flash, session
import requests
from logic.user_logic import UserLogic
import datetime

logic = UserLogic()


class DashboardRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/index")
        def dashboard():
            return render_template("dashboard.html")

        @app.route("/clientDashboard")
        def adminDashboard():
            return render_template("clientDashboard.html")

        @app.route("/adminDashboard")
        def clientMenu():
            return render_template("adminDashboard.html")

        @app.route("/adminMenu")
        def adminMenu():
            return render_template("adminMenu.html")

        @app.route("/insertService", methods=["GET", "POST"])
        def insertService():
            if request.method == "GET":
                return render_template("insertService.html")
            elif request.method == "POST":
                titulo = request.form["titulo"]
                descripcion = request.form["descripcion"]
                logic.insertService(titulo, descripcion)
                servicios = logic.getAllServices()
                return render_template("serviciosAdmin.html", servicios = servicios)

        @app.route("/landingPage")
        def landingPage():
            return render_template("landingPage.html")

        @app.route("/serviciosAdmin", methods=["GET", "POST"])
        def serviciosAdmin():
            if request.method == "GET":
                servicios = logic.getAllServices()
                return render_template("serviciosAdmin.html", servicios = servicios)
            if request.method == "POST":
                serviceId = request.form["id"]
                logic.deleteService(serviceId)
                servicios = logic.getAllServices()
                return render_template("serviciosAdmin.html", servicios = servicios)

        @app.route("/reservacionesAdmin")
        def reservacionesAdmin():
            return render_template("reservacionesAdmin.html")

        @app.route("/tablareservaciones", methods=["GET", "POST"])
        def tablareservaciones():
            usuario = session["login_user"]
            if request.method == "GET":
                getAllReservations = logic.getAllReservations()
                return render_template("tablareservaciones.html", reservacion = getAllReservations, usuario = usuario)
            if request.method == "POST":
                id = request.form["id"]
                logic.deleteReservation(id)
                getAllReservations = logic.getAllReservations()
                return render_template("tablareservaciones.html", reservacion = getAllReservations, usuario = usuario)

        @app.route("/reservacion", methods=["GET", "POST"])
        def reservacion():
            if request.method == "GET":
                servicios = logic.getAllServices()
                return render_template("reservacion.html", servicios = servicios)
            if request.method == "POST":
                    usuario = session["login_user"]
                    fecha = request.form["fecha"]
                    servicio = request.form["servicioss"]
                    pasajeros = request.form["pasajeros"]
                    pasajeros = str(pasajeros)
                    partida = request.form["partida"]
                    destino = request.form["destino"]
                    logic.insertReservation(usuario, fecha, servicio, fecha, partida, destino)
                    getAllReservations = logic.getAllReservations()
                    return render_template("tablareservaciones.html", reservacion = getAllReservations, usuario = usuario)

        @app.route("/perfilCliente")
        def perfilCliente():
                return render_template("perfilCliente.html")

        @app.route("/contact")
        def contact():
                return render_template("contact.html")

        @app.route("/servicios")
        def servicios():
                return render_template("servicios.html")

        @app.route("/info")
        def info():
                return render_template("info.html")

        @app.route("/tablaReservAdmin")
        def tablaReservAdmin():
                if request.method == "GET":
                    getAllReservations = logic.getAllReservations()
                    return render_template("tablaReservAdmin.html", reservacion = getAllReservations)

        @app.route("/logout")
        def logout():
            if session.get("loggedIn"):
                session.pop("loggedIn")
                return redirect("login")
            else:
                return redirect("login")

        if __name__ == "__main__":
            app.run(debug=True)
