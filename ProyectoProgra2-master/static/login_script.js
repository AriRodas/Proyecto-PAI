function checkLogin(){
    var user = document.getElementById("user").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("passw").value;

    var userArray = JSON.parse(localStorage.getItem("localUser"));

    if(user !== null && user!== "" ){
        if(email !== null && email!== "" ){
            if(password !== null && password !== ""){
                var canLogin = checkLoginInfo(user, email, password, userArray);
                if(canLogin === true){
                    createSessionUser(user, email, password, "client")
                    window.location.href="/index_cliente";
                }else{
                    admin(user, email, password)
                }
            }else{
                alert("La contraseña no puede estar vacía");
            }
        }else{
            alert("El correo no puede estar vacío");
        }
    }else{
        alert("El usuario no puede estar vacío");
    }
}

function admin(user, email, password){

    var userArray = JSON.parse(localStorage.getItem("lUserArray"));

    if(user == "quality_transport" ){
        if(email == "ventas@qtransportsv.com" ){
            if(password == "qtsv2011"){
                var canLogin = checkLoginInfo(user, email, password, userArray);
                if(canLogin === true){
                    createSessionAdmi(user, email, password)
                    window.location.href="/index_admi";
                }else{
                    alert("El usuario, correo o contraseña son incorrectos");
                }
            }else{
                alert("La contraseña no puede estar vacía");
            }
        }else{
            alert("El correo no puede estar vacío");
        }
    }
    else{
        alert("No válido")
    }
}


    


function checkLoginInfo(user, email, password, userArray){
    if(userArray!==null && userArray.length > 0){
        for(var i=0; i<userArray.length; i++){
            if(userArray[i].user===user && userArray[i].email===email && userArray[i].password === password){
                return true;
            }
        }
    }
    return false;
}

function createSessionUser(user, email, password, role) {
    var logged_user = {
        user: user,
        email: email,
        password: password,
        role: role
    }
    sessionStorage.setItem("wUserArray", JSON.stringify(logged_user));
}

function createSessionAdmi(user, email, password) {
    var logged_admi = {
        user: "quality_transport",
        email: "ventas@qtransportsv.com",
        password:"qtsv2011",
        role: "admin"
    };
    sessionStorage.setItem("wUserArray", JSON.stringify(logged_admi));
}
