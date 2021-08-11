from flask import Flask, render_template, redirect, request, url_for, flash, session
import requests
from logic.user_logic import UserLogic


class PaquetesROutes:
    @staticmethod
    def configure_routes(app):

        @app.route("/opcionesHotel", methods=["GET", "POST"])
        def opcionesHotel():
            if request.method == "GET":
                return render_template("opcionesHotel.html")
            elif request.method == "POST":
                option = request.form["option"]
                if option == "Si":
                    return render_template("selectHotel.html")
                elif option == "No":
                    return render_template("opcionesLugares.html")

        @app.route("/selectHotel", methods=["GET", "POST"])
        def selectHotel():
            if request.method == "GET":
                return render_template("selectHotel.html")
            elif request.method == "POST":
                lugar = request.form["lugar"]
                response = requests.get("https://restapi-titanio.herokuapp.com/hotel/" + lugar)
                dataJson = response.json()
                return render_template("tablaHotel.html", dataJson = dataJson)

        @app.route("/tablaHotel", methods=["GET", "POST"])
        def tablaHotel():
            if request.method == "GET":
                return render_template("tablaHotel.html")
            elif request.method == "POST":
                hotel = request.form["hotel"]
                return render_template("opcionesLugares.html", hotel = hotel)

        @app.route("/opcionesLugares", methods=["GET", "POST"])
        def opcionesLugares():
            if request.method == "GET":
                return render_template("opcionesLugares.html")
            elif request.method == "POST":
                option = request.form["option"]
                if "hotel" in request.form:
                    hotel = request.form["hotel"]
                if option == "Si":
                    return render_template("selectLugares.html", hotel = hotel)
                elif option == "No":
                    return render_template("opcionesGuia.html", hotel = hotel)

        @app.route("/selectLugares", methods=["GET", "POST"])
        def selectLugares():
            if request.method == "GET":
                return render_template("selectLugares.html")
            elif request.method == "POST":
                hotel = ""
                if "hotel" in request.form:
                    hotel = request.form["hotel"]
                lugar = request.form["lugar"]
                response = requests.get("https://restapi-titanio.herokuapp.com/tour/" + lugar)
                dataJson = response.json()
                return render_template("tablaLugares.html", dataJson = dataJson, hotel = hotel)


        @app.route("/tablaLugares", methods=["GET", "POST"])
        def tablaLugares():
            if request.method == "GET":
                return render_template("tablaLugares.html")
            elif request.method == "POST":
                hotel = ""
                lugar = ""
                if "hotel" in request.form:
                    hotel = request.form["hotel"]
                if "lugar" in request.form:
                    lugar = request.form["lugar"]
                return render_template("opcionesGuia.html", hotel = hotel, lugar = lugar)

        @app.route("/opcionesGuia", methods=["GET", "POST"])
        def opcionesGuia():
            if request.method == "GET":
                return render_template("opcionesGuia.html")
            elif request.method == "POST":
                hotel = ""
                lugar = ""
                option = request.form["option"]
                if "hotel" in request.form:
                    hotel = request.form["hotel"]
                if "lugar" in request.form:
                    lugar = request.form["lugar"]
                if option == "Si":
                    return render_template("selectGuia.html", hotel = hotel, lugar = lugar)
                elif option == "No":
                    return render_template("resumenPaquetes.html", hotel = hotel, lugar = lugar)

        @app.route("/selectGuia", methods=["GET", "POST"])
        def selectGuia():
            if request.method == "GET":
                return render_template("selectLugares.html")
            elif request.method == "POST":
                hotel = ""
                lugar = ""
                guia = ""
                pago = 0
                if "hotel" in request.form:
                    hotel = request.form["hotel"]
                    pago = pago + 5
                if "lugar" in request.form:
                    lugar = request.form["lugar"]
                    pago = pago + 5
                if "guia" in request.form:
                    guia = request.form["guia"]
                    pago = pago + 5
                return render_template("resumenPaquetes.html", hotel = hotel, lugar = lugar, guia = guia, pago = pago)

        @app.route("/resumenPaquetes", methods=["GET", "POST"])
        def resumenPaquetes(hotel, lugar, guia):
            if request.method == "GET":
                return render_template("resumenPaquetes.html")
            elif request.method == "POST":
                hotel = ""
                lugar = ""
                guia = ""
                pago = 0
                if "hotel" in request.form:
                    hotel = request.form["hotel"]
                    pago = pago + 5
                if "lugar" in request.form:
                    lugar = request.form["lugar"]
                    pago = pago +5
                if "guia" in request.form:
                    guia = request.form["guia"]
                    pago = pago +5
                print(pago)
                return render_template("resumenPaquetes.html", hotel = hotel, lugar = lugar, guia = guia, pago = pago)
