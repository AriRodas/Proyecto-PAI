function reservaciones(){
    var fecha = document.getElementById("fecha").value;
    var pasajeros = document.getElementById("pasajeros").value;
    var destino = document.getElementById("destino").value;
    var servicios = document.getElementById("servicios").value;
    var partida= document.getElementById("partida").value;

    var RuserArray = [];

    if(localStorage.getItem("PSUserArray")!==null){
        RuserArray = JSON.parse(localStorage.getItem("PSUserArray"));
    }

    var current_user = JSON.parse(sessionStorage.getItem("wUserArray"))


    var current_reg = {
        lfecha: fecha,
        user: current_user.user,
        lpasajeros: pasajeros,
        ldestino: destino,
        lservicios: servicios,
        lpartida: partida

    };

    RuserArray.push(current_reg);

    localStorage.setItem("PSUserArray", JSON.stringify(RuserArray));

    alert("su reservacion ha sido tomada con exito")

}

function tablita(){
    checkForValidLoginSession()
    var Stable = JSON.parse(localStorage.getItem("PSUserArray"))

    var user = JSON.parse(sessionStorage.getItem("wUserArray"))
    

    for(var i = 0; i < Stable.length; i++){

        if(Stable[i] !== null){

            if(user.role == "client"){
                if(user.user == Stable[i].user){
                    table(Stable, i, user)
                }
            }else{
                table(Stable, i, user)
            }
        }

    }
}

function table(Stable, i, user){
    var table = document.getElementById("myTable")

    var newRow = table.insertRow(1)

    var cell0 = newRow.insertCell(0)
    var cell1 = newRow.insertCell(1)
    var cell2 = newRow.insertCell(2)
    var cell3 = newRow.insertCell(3)
    var cell4 = newRow.insertCell(4)
    var cell5 = newRow.insertCell(5)
    

    if(user.role == "client"){
        var cell6 = newRow.insertCell(6)
        cell6.setAttribute("type", "span")
        cell6.setAttribute("id", "deleteTable")
        cell6.innerHTML = "&times;";
        cell6.setAttribute("onclick", "deleteRow(" + i + ")")
        newRow.appendChild(cell6);
    }
    
    
    cell0.innerHTML = Stable[i].user
    cell1.innerHTML = Stable[i].lfecha
    cell2.innerHTML = Stable[i].lservicios
    cell3.innerHTML = Stable[i].lpasajeros
    cell4.innerHTML = Stable[i].lpartida
    cell5.innerHTML = Stable[i].ldestino
}

function deleteTable(){
    var rowCount = document.getElementById("myTable").rows.length;


    if(rowCount > 1){
        deleteAllTable(rowCount)
        tablita()
    }
    else{
        tablita()
    }
}

function deleteAllTable(row) {

    while (row !== 1) {
        document.getElementById("myTable").deleteRow(1);
        row--
    }
    

}

function deleteRow(i) {

    roomArray = JSON.parse(localStorage.getItem("PSUserArray"));

    delete roomArray[i]

    localStorage.setItem("PSUserArray", JSON.stringify(roomArray));

    deleteTable()
}


function checkForValidLoginSession() {

    if (sessionStorage.getItem("wUserArray") == null) {
        window.location.href = "/login"
    }
}

function logout() {
    sessionStorage.removeItem("wUserArray")
    window.location.href = "/"
}
