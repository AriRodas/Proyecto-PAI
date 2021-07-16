from core.pyba_logic import PybaLogic


class UserLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertUser(self, user, email, password, salt):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `quality_transport`.`user` "
            + "(`id`,`user_name`,`email`,`role`,`password`,`salt`) "
            + f"VALUES(0,'{user}','{email}','client','{password}','{salt}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def insertEvent(self, eventName, client, date, numberOfPeople):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `hotel`.`event` "
            + "(`id`,`event_name`,`user`,`date`,`number_of_people`) "
            + f"VALUES(0,'{eventName}','{client}','{date}',{numberOfPeople});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def insertService(self, titulo, descripcion):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `quality_transport`.`servicios` "
            + "(`id`,`titulo`,`descripcion`) "
            + f"VALUES(0,'{titulo}', '{descripcion}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def insertReservation(self, usuario, fecha, servicio, pasajeros, partida, destino):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `quality_transport`.`reservacion` "
            + "(`id`,`usuario`,`fecha`, `servicio`, `pasajeros`, `partida`, `destino`) "
            + f"VALUES(0,'{usuario}', '{fecha}', '{servicio}', {pasajeros}, '{partida}', '{destino}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getUser(self, user):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM quality_transport.user where user_name = '{user}';"
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []

    def getAllServices(self):
        database = self.createDatabaseObj()
        sql = "select * from quality_transport.servicios;"
        result = database.executeQuery(sql)
        return result

    def deleteService(self, id):
        database = self.createDatabaseObj()
        sql = f"delete FROM quality_transport.servicios where id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows
    
    def deleteReservation(self, id):
        database = self.createDatabaseObj()
        sql = f"delete FROM quality_transport.reservacion where id = {id};"
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAllReservations(self):
        database = self.createDatabaseObj()
        sql = "select * from quality_transport.reservacion;"
        result = database.executeQuery(sql)
        return result

    