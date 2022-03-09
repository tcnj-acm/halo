const wholeForm = document.querySelector(".form-whole")
const formPages = [...wholeForm.querySelectorAll(".form-page")]
let currentPage = formPages.findIndex(page =>{
    return !page.classList.contains("d-none")
}) 

if(currentPage < 0){
    currentPage = 0
    showCurrentPage()
}

wholeForm.addEventListener("click", event =>{
    let increment
    let allValid = true
    if(event.target.matches("[data-next-button]")){
        increment = 1
        const inputFeilds = [...formPages[currentPage].querySelectorAll("input")]
        allValid = inputFeilds.every(input => input.reportValidity())
    }else if (event.target.matches("[data-previous-button]")){
        increment = -1
    } if (increment == null) return

    if(allValid){
        currentPage += increment
        showCurrentPage()
    }
})

function showCurrentPage(){
    formPages.forEach((page, index) => {
        page.classList.toggle("d-none", index != currentPage)
    })
}    

function youngDate(){
    const birthDate = new Date(document.getElementById("id_date_of_birth").value)
    const today = new Date('4/9/2022')

    var age = today.getFullYear() - birthDate.getFullYear()
    const month = today.getMonth() - birthDate.getMonth()
    const day = today.getDate() - birthDate.getDate()
    if((month < 0 || (month === 0 && day < 0))){
        age--;
    }
    if(age < 18){
        dateSection = document.getElementById("date-check")
        dateSection.classList.remove("d-none")
    }else{
        dateSection = document.getElementById("date-check")
        dateSection.classList.add("d-none")
    }
    document.getElementById("id_age").value = age
}

function formSubmission(){
    const formSubmission = document.getElementById("formSubmission")
    var selects = [...formSubmission.querySelectorAll('input')]
    selects.pop()
    if(document.getElementById("date-check").classList.contains("d-none")){
        selects.pop()
    }

    allValid = selects.every(input => input.checked)

    const submissionButton = document.getElementById("submissionButton")
    if(allValid){
        submissionButton.removeAttribute("disabled")
    }else{
        submissionButton.setAttribute("disabled", "")
    }
}