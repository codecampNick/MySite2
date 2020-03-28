function testingThis(){
    console.log("From a function!");
}

function toggleVisibility(id, textId){
    let status = document.getElementById(id).style.display;
    console.log(status);
    if(status === "none"){
        console.log("should display");
        //document.getElementById(id).style.display = "";
        let el = document.getElementById(id);
        //
        el.style.opacity = 0
        el.style.display = '';
        let op = 0.1;  // initial opacity
        let timer = setInterval(function () {
            if (op >= 1){
                clearInterval(timer);
            }
            el.style.opacity = op;
            el.style.filter = 'alpha(opacity=' + op * 100 + ")";
            op += op * 0.1;
        }, 20);
        //
        $(textId).html("show less&#8230;");
    }
    else{
        console.log("should hide");
        $(textId).html("show more&#8230;");
        //document.getElementById(id).style.display = "none";
        let el = document.getElementById(id);
        //
        let op = 1;  // initial opacity
        let timer = setInterval(function () {
            if (op <= 0.1){
                clearInterval(timer);
                el.style.display = 'none';
            }
            el.style.opacity = op;
            el.style.filter = 'alpha(opacity=' + op * 100 + ")";
            op -= op * 0.1;
        }, 50);
        //
    }
}

$(document).ready(function(){
    //alert("from js folder");
    //testingThis();
    $("#health-ecareers-header").click(function(){
        toggleVisibility("health-ecareers-body", "#health-ecareers-header");
    });

    $("#dice-holdings-inc-header").click(function(){
        toggleVisibility("dice-holdings-inc-body", "#dice-holdings-inc-header");
    });

    $("#ontargetjobs-header").click(function(){
        toggleVisibility("ontargetjobs-body", "#ontargetjobs-header");
    });

    $("#aerios-direct-inc-header").click(function(){
        toggleVisibility("aerios-direct-inc-body", "#aerios-direct-inc-header");
    });
});