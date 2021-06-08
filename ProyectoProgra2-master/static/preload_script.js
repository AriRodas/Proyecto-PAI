function preLoadUsers() {

    var userArray = [{
        user: "quality_transport",
        email: "ventas@qtransportsv.com",
        password: "qtsv2011",
        role: "admin",
    }]

    localStorage.setItem("lUserArray", JSON.stringify(userArray))
}

preLoadUsers()