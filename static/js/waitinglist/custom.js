let captchaDone = false;
function captchaIsComplete() {
    captchaDone = true;
    formSubmission();
}

function captchaHasFailed() {
    captchaDone = false;
    formSubmission();
}

function initRecaptcha() {
    grecaptcha.render(
        'myCaptcha',
        {
            sitekey: '6Ld-pxgqAAAAAE8PyIymjrQQnSZiH4DI-KAHPSyK',
            callback: captchaIsComplete,
            'expired-callback': captchaHasFailed,
            'reset-callback': captchaHasFailed,
        }
    );
}

const waitingForm = document.getElementById("waitingListForm")
const emailField = waitingForm.querySelector('input[name="email"]');
const fullNameField = waitingForm.querySelector('input[name="full_name"]');

emailField.addEventListener("input", formSubmission);
fullNameField.addEventListener("input", formSubmission)

function formSubmission() {
    const emailValid = emailField && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailField.value);
    const fullNameValid = fullNameField && fullNameField.value.trim() !== "";

    console.log(emailValid);
    console.log(fullNameValid)
    console.log(captchaDone);
    const allFieldsValid = emailValid && fullNameValid;

    const submissionButton = document.getElementById("formSubmission")
    if (captchaDone && allFieldsValid) {
        submissionButton.removeAttribute("disabled")
        submissionButton.classList.remove("btn-secondary")
        submissionButton.classList.add("btn-primary")
    } else {
        submissionButton.setAttribute("disabled", "")
        submissionButton.classList.remove("btn-primary")
        submissionButton.classList.add("btn-secondary")
    }
}



window.onload = function () {
    var recaptchaScript = document.createElement('script');
    recaptchaScript.src = 'https://www.google.com/recaptcha/api.js?onload=initRecaptcha&render=explicit';
    recaptchaScript.async = true;
    recaptchaScript.defer = true;
    document.body.appendChild(recaptchaScript);
};

