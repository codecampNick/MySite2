$(document).ready(function(){
    console.log("Hi");
    let parkerRequest = new XMLHttpRequest();
    parkerRequest.open("GET", 'https://api.weather.gov/stations/KAPA/observations/latest', true)
    parkerRequest.onload = function(){
        let data = JSON.parse(this.response);
        let curCond = data.properties.textDescription;
        let tempInF = parseFloat((data.properties.temperature.value * 1.8) + 32).toFixed(1);
        let parkerTime = new Date(data.properties.timestamp).toLocaleString("en-US", {timeZone: "America/Denver"});
        $("#parkerTime").append(parkerTime);
        $("#parkerCurrentCond").append(curCond);
        $("#parkerTemp").append(tempInF);
    };
    parkerRequest.send();
    console.log("kona request")
    let konaRequest = new XMLHttpRequest();
    konaRequest.open("GET", 'https://api.weather.gov/stations/PHKO/observations/latest', true);
    konaRequest.onload = function(){
        let kdata = JSON.parse(this.response);
        let kCurrentCond = kdata.properties.textDescription;
        let kTempInF = parseFloat((kdata.properties.temperature.value * 1.8) + 32).toFixed(1);
        let konaTime = new Date(kdata.properties.timestamp).toLocaleString("en-US", {timeZone: "Pacific/Honolulu"});

        $("#konaTime").append(konaTime);
        $("#konaCurrentCond").append(kCurrentCond);
        $("#konaTemp").append(kTempInF);
    };
    konaRequest.send();
});