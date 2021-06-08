function registerNewUser(){
    var reg_user = document.getElementById("user_reg").value;
    var reg_email = document.getElementById("email_reg").value;
    var reg_password = document.getElementById("passw_reg").value;

    alert("Usted se ha registrado como "+reg_user);
    var userArray = [];

    if(localStorage.getItem("localUser")!==null){
        userArray = JSON.parse(localStorage.getItem("localUser"));
    }

    var current_reg = {
        user: reg_user,
        email: reg_email,
        password: reg_password,
        role: "client"
    };

    userArray.push(current_reg);


    localStorage.setItem("localUser", JSON.stringify(userArray));
}
