$(document).ready(function(){
    console.log("Hi");
    let parkerRequest = new XMLHttpRequest();
    parkerRequest.open("GET", 'https://api.weather.gov/stations/KAPA/observations/latest', true)
    parkerRequest.onload = function(){
        let data = JSON.parse(this.response);
        console.log(JSON.stringify(data));
        console.log(data.properties.temperature.value)
        let curCond = data.properties.textDescription;
        let tempInF = (data.properties.temperature.value * 1.8) + 32;
        let parkerTime = new Date(data.properties.timestamp).toLocaleString("en-US", {timeZone: "America/Denver"});
        console.log(tempInF);
        $("#parker").append("Parker<br />Last Updated: " + parkerTime + "<br />Current Conditions: " + curCond + "<br />Temp: " + parseFloat(tempInF).toFixed(1) + "&deg;" );
    };
    parkerRequest.send();
    console.log("kona request")
    let konaRequest = new XMLHttpRequest();
    konaRequest.open("GET", 'https://api.weather.gov/stations/PHKO/observations/latest', true);
    konaRequest.onload = function(){
        let kdata = JSON.parse(this.response);
        let kCurrentCond = kdata.properties.textDescription;
        let kTempInF = (kdata.properties.temperature.value * 1.8) + 32;
        let konaTime = new Date(kdata.properties.timestamp).toLocaleString("en-US", {timeZone: "Pacific/Honolulu"});
        $("#kona").append("Kona<br />Last Updated: " + konaTime + "<br />Current Conditions: " + kCurrentCond + "<br />Temp: " + parseFloat(kTempInF).toFixed(1) + "&deg;" );
    };
    konaRequest.send();
});