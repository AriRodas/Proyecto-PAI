function logout() {
    sessionStorage.removeItem("wUserArray")
    window.location.href = "/"
}