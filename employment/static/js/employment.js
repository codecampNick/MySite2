function testingThis(){
    console.log("From a function!");
}

function toggleVisibility(id, textId){
    let status = document.getElementById(id).style.display;
    console.log(status);
    if(status === "none"){
        console.log("should display");
        document.getElementById(id).style.display = "";
        $(textId).html("show less&#8230;");
    }
    else{
        console.log("should hide");
        document.getElementById(id).style.display = "none";
        $(textId).html("show more&#8230;");
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