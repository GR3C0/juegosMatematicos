$("#login_button").onclick;

function check_pass(){
    grupo = document.getElementById("grupo").value;
    pass = document.getElementById("pass").value;
    fetch("/login_user/"+grupo+"/"+pass)
    .then(function(){
        console.log("hecho")
    })
}