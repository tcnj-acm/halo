const MAX_WIDTH = decideCurr()
function onPage(sizes){
    xl = window.matchMedia("(min-width: 999px) and (max-width: 3000px)");
    l = window.matchMedia("(min-width: 760px) and (max-width: 999px)");
    if(xl.matches){
        document.getElementById("width-control").style.maxWidth = sizes[0]
    }else if(l.matches){
        document.getElementById("width-control").style.maxWidth = sizes[1]
    }
    return
}

function returnOrigin(){
    document.getElementById("width-control").style.maxWidth = MAX_WIDTH
}

function decideCurr(){
    let curr = "90%"
    if(window.matchMedia("(min-width: 999px) and (max-width: 3000px)").matches){
        curr = "60%"
    }else if(window.matchMedia("(min-width: 760px) and (max-width: 999px)").matches){
        curr = "80%"
    }else if(window.matchMedia("(min-width: 530px) and (max-width: 759px)").matches){
        curr = "85%"
    }else if(window.matchMedia("(min-width: 359px) and (max-width: 376px)").matches){
        curr = "85%"
    }else if(window.matchMedia("(max-width: 290px)").matches){
        curr = "100%"
    }
    return curr
}

