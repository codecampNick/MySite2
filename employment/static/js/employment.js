$(document).ready(function(){

    document.getElementById("employment-container").addEventListener('click', function(event){
        if(event.target.classList.contains('show-hide')){
            let el = event.target.parentElement;
            let nextEl = el.nextElementSibling;
            let status = nextEl.style.display;
            console.log(status);
            if(status === 'none'){
                nextEl.style.opacity = 0
                nextEl.style.display = '';
                let op = 0.1;  // initial opacity
                let timer = setInterval(function () {
                    if (op >= 1){
                        clearInterval(timer);
                    }
                    nextEl.style.opacity = op;
                    nextEl.style.filter = 'alpha(opacity=' + op * 100 + ")";
                    op += op * 0.1;
                }, 20);
                event.target.innerText = "(show less...)";
            }
            else{
                event.target.innerText = "(show more...)"
                let op = 1;  // initial opacity
                let timer = setInterval(function () {
                    if (op <= 0.1){
                        clearInterval(timer);
                        nextEl.style.display = 'none';
                    }
                    nextEl.style.opacity = op;
                    nextEl.style.filter = 'alpha(opacity=' + op * 100 + ")";
                    op -= op * 0.1;
                }, 50);
            }
        }
    }, false);
});