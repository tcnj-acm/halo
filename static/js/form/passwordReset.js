

pwr = document.getElementById("password_reset")//
pwrsc = document.getElementById("password_reset_success")
pwrs = document.getElementById("password_reset_sent")//
pwrf = document.getElementById("password_reset_form")

if(pwr){
    onPage(["30%","50%"])//
}else if(pwrsc){
    onPage(["40%","50%"])
}else if(pwrs){
    onPage(["30%","50%"])//
}else if(pwrf){
    onPage(["30%","50%"])//
    document.addEventListener('DOMContentLoaded', function () {
        document.querySelector("#id_new_password2").oninput = checkNewPassword2;
    }, false);
}


function checkNewPassword2(event) {
    password = document.getElementById("id_new_password1").value
    passwordCheckErrorContainer = document.getElementById("new_password2_error_label")

    if (event.target.value != password) {
        event.target.classList.add("is-invalid")
        passwordCheckErrorContainer.classList.remove("d-none")
    } else {
        event.target.classList.remove("is-invalid")
        passwordCheckErrorContainer.classList.add("d-none")
    }
}