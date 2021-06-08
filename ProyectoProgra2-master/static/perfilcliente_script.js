function datos(){

    var RuserArray = [];

    if(localStorage.getItem("PSUserArray")!==null){
        RuserArray = JSON.parse(localStorage.getItem("PSUserArray"));
    }

    var current_user = JSON.parse(sessionStorage.getItem("wUserArray"))
    var current_email =JSON.parse(sessionStorage.getItem("wUserArray"))


    var current_reg = {
        user: current_user.user,
        email: current_email.email
    };
    
    RuserArray.push(current_reg);
    localStorage.setItem("PSUserArray", JSON.stringify(RuserArray));
}

function tablita2(){
    datos()
    checkForValidLoginSession()
    var Stable = JSON.parse(localStorage.getItem("PSUserArray"))
    var user = JSON.parse(sessionStorage.getItem("wUserArray"))
    for(var i = 0; i < Stable.length; i++){

        if(Stable[i] !== null){

            if(user.user == Stable[i].user){
                var table = document.getElementById("myTable")

                var newRow = table.insertRow(1)

                var cell0 = newRow.insertCell(0)
                var cell1 = newRow.insertCell(1)
                newRow.appendChild(cell1);
                cell0.innerHTML = Stable[i].user
                cell1.innerHTML = user.email
            }
            
        }
        if(i>1){
            break
        }
    }
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