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
    const date = document.getElementById("id_date_of_birth").value

}