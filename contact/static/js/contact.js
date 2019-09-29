function charCount(count){
        var remaining = (255 - count);
        $("#num").html(remaining);
}

$(document).ready(function(){

    $("#id_from_name").on("keyup", function(){
        var remaining = (100 - this.value.length);
        $("#from_name_count").html(remaining);
        console.log(remaining);
    });

    $("#id_from_email").on("keyup", function(){
        var remaining = (255 - this.value.length);
        $("#from_email_count").html(remaining);
        console.log(remaining);
    });

    $("#id_subject").on("keyup", function(){
        var remaining = (255 - this.value.length);
        $("#subject_count").html(remaining);
        console.log(remaining);
    });

    $("#id_message").on("keyup", function(){
        var remaining = (5000 - this.value.length);
        $("#message_count").html(remaining);
        console.log(remaining);
    });
});