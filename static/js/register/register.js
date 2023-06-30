function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const wholeForm = document.querySelector(".form-whole")
const formPages = [...wholeForm.querySelectorAll(".form-page")]
let pageInfo = {
    currentPage: -1,
    pageValidationStatus: true,
    individualValidation: new Map([
        [0, true],
        [1, true],
        [2, false],
        [3, true],
        [4, true]
    ]),
    errors: new Map([
        [0, []],
        [1, []],
        [2, []],
        [3, []]
    ])
};
if (pageInfo.currentPage < 0) {
    pageInfo.currentPage = 0;
    showCurrentPage();
}
pageInfo.currentPage = formPages.findIndex(page => {
    return !page.classList.contains("d-none")
})

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector("#id_password2").oninput = checkPassword2;
}, false);

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector("#id_resume").onchange = checkResume;
}, false);

window.addEventListener("load", function () {
    setTimeout(function () {
        youngDate()
    }, 500);
});

wholeForm.addEventListener("click", event => {


    let increment = 0
    pageInfo.pageValidationStatus = true
    if (event.target.matches("[data-next-button]")) {
        increment = 1
        const inputFields = [...formPages[pageInfo.currentPage].querySelectorAll("input")]
        pageInfo.pageValidationStatus = inputFields.every(input => input.reportValidity())
    } else if (event.target.matches("[data-previous-button]")) {
        increment = -1
    } if (increment == null) return


    generalErrorText = document.getElementById("error-reminder-container");
    if (pageInfo.pageValidationStatus && pageInfo.individualValidation.get(pageInfo.currentPage)) {
        generalErrorText.classList.add("d-none")
        pageInfo.currentPage += increment;
        showCurrentPage();
    } else {
        generalErrorText.classList.remove("d-none")
    }
})


function showCurrentPage() {
    formPages.forEach((page, index) => {
        page.classList.toggle("d-none", index != pageInfo.currentPage)
    })
    if (pageInfo.currentPage == 4) {
        onPage(["40%", "60%"]);
    } else {
        returnOrigin();
    }
}

function youngDate() {
    const age = document.getElementById("id_age").value;
    if (age < 18) {
        dateSection = document.getElementById("date-check")
        dateSection.classList.remove("d-none")
    } else {
        dateSection = document.getElementById("date-check")
        dateSection.classList.add("d-none")
    }
}

function formSubmission() {
    const formSubmission = document.getElementById("formSubmission")
    var selects = [...formSubmission.querySelectorAll('.req-input')]
    if (document.getElementById("date-check").classList.contains("d-none")) {
        selects.pop()
    }

    let allChecked = selects.every(input => input.checked)

    const submissionButton = document.getElementById("submissionButton")
    if (allChecked) {
        submissionButton.removeAttribute("disabled")
        submissionButton.classList.remove("btn-secondary")
        submissionButton.classList.add("btn-primary")
    } else {
        submissionButton.setAttribute("disabled", "")
        submissionButton.classList.remove("btn-primary")
        submissionButton.classList.add("btn-secondary")
    }
}

async function emailValidation() {
    emailInput = document.getElementById("id_email")
    email = emailInput.value


    if (!emailInput.reportValidity()) {
        emailInput.focus();
        return
    }

    validation = postData("/get/json/email/verification", { "email": emailInput.value })

    await validation.then(function (result) {
        let x = result
        pageInfo.individualValidation.set(pageInfo.currentPage, x.valid)
        pageInfo.errors.set(pageInfo.currentPage, x.message)
    })
    emailError = document.getElementById("email_error_label")
    if (pageInfo.individualValidation.get(pageInfo.currentPage)) {
        emailError.classList.add("d-none")
        emailInput.classList.remove("is-invalid")
        return
    } else {
        emailInput.classList.add("is-invalid")
        emailError.classList.remove("d-none")
        emailInput.focus();
    }
}

async function passwordValidation() {
    passwordInput = document.getElementById("id_password1")
    validation = postData("/get/json/password/verification", { "p1": passwordInput.value })
    await validation.then(function (result) {
        let x = result
        pageInfo.individualValidation.set(pageInfo.currentPage, x.valid)
        pageInfo.errors.set(pageInfo.currentPage, x.errors)
    })
    passwordErrorContainer = document.getElementById("password-container")
    passwordErrorList = document.getElementById("password-list")
    if (pageInfo.individualValidation.get(pageInfo.currentPage)) {
        passwordInput.classList.remove("is-invalid")
        passwordErrorContainer.classList.add("d-none")
        removeAllChildNodes(passwordErrorList);
        return
    } else {
        passwordInput.focus();
        removeAllChildNodes(passwordErrorList);
        pageInfo.errors.get(pageInfo.currentPage).forEach((error) => {
            let li = document.createElement("li");
            li.setAttribute('class', 'list-group-item list-group-item-danger')
            li.innerHTML = error;
            passwordErrorList.appendChild(li);
        })
        passwordErrorContainer.classList.remove("d-none")
        passwordInput.classList.add("is-invalid")
        return
    }
}

function checkPassword2(event) {
    password = document.getElementById("id_password1").value
    passwordCheckErrorContainer = document.getElementById("password2_error_label")

    if (event.target.value != password) {
        event.target.classList.add("is-invalid")
        passwordCheckErrorContainer.classList.remove("d-none")
    } else {
        event.target.classList.remove("is-invalid")
        passwordCheckErrorContainer.classList.add("d-none")
    }
}

function password2Validation() {
    password = document.getElementById("id_password1").value
    password2 = document.getElementById("id_password2")
    if (password2.value != password) {
        pageInfo.individualValidation.set(pageInfo.currentPage, false);
    } else {
        pageInfo.individualValidation.set(pageInfo.currentPage, true);
    }
}

function removeAllChildNodes(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}

const fileTypes = [
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/msword",
    "application/pdf"
]

function checkResume(event) {
    let file = event.target.files[0]
    resumeError = document.getElementById("resume_error")

    if (file === undefined) {
        pageInfo.individualValidation.set(pageInfo.currentPage, false);
        event.target.classList.add("is-invalid")
        resumeError.classList.remove("d-none")
    } else if (fileTypes.includes(file.type)) {
        pageInfo.individualValidation.set(pageInfo.currentPage, true);
        resumeError.classList.add("d-none")
        event.target.classList.remove("is-invalid")
    } else {
        pageInfo.individualValidation.set(pageInfo.currentPage, false);
        event.target.classList.add("is-invalid")
        resumeError.classList.remove("d-none")
    }
}

async function postData(url, data) {
    var x = await fetch(url, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            data
        })
    }).then(function (response) {
        return response.json();
    }).then(function (data) {
        return data
    }).catch(function (err) {
        console.log(err);
    })
    return (x)
}
