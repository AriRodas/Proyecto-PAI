from flask import Flask, render_template, redirect, request, url_for, flash, session
import requests
from logic.user_logic import UserLogic
import datetime
from logic.user_logic import UserLogic

logic = UserLogic()

class checkoutRoutes:
    @staticmethod
    def configure_routes(app):

        @app.route("/checkout", methods=["GET", "POST"])
        def checkout():
            login_user = session["login_user"]
            if request.method == "GET":
                return 1
            elif request.method == "POST":
                pago = request.form["pago"]
                return render_template("checkout2.html", pago = pago)

        @app.route("/checkout2", methods=["GET", "POST"])
        def checkout2():
            login_user = session["login_user"]
            if request.method == "GET":
                return render_template("checkout2.html")
            elif request.method == "POST":

                name = request.form["name"]
                creditCard = request.form["creditCard"]
                date = request.form["date"]
                code = request.form["code"]
                balance = request.form["pago"]
                balance = int(balance)

                data = {
                    "name": name,
                    "number": creditCard,
                    "date": date,
                    "code": code,
                    "balance": balance
                }

                response = requests.post("http://credit-card-auth-api-cerberus.herokuapp.com/verify", data=data)
                print(response)
                if response.status_code == 200:
                    dataJson = response.json()
                    print(dataJson['response'])
                    if dataJson['response'] == '00':
                        return render_template("tarjeta.html")
                    else:
                        return render_template("error.html")
                else:
                    return render_template("error.html")