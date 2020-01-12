function convertTemp(temp){
    return temp == null? "No Info": parseFloat((temp * 1.8) + 32).toFixed(1) + "&deg;";
};

$(document).ready(function(){
    console.log("Hi");
    let parkerRequest = new XMLHttpRequest();
    parkerRequest.open("GET", 'https://api.weather.gov/stations/KAPA/observations/latest', true)
    parkerRequest.onload = function(){
        let data = JSON.parse(this.response);
        let curCond = data.properties.textDescription;
        let tempInF = data.properties.temperature.value;
        tempInF = convertTemp(tempInF);
        let parkerTime = new Date(data.properties.timestamp).toLocaleString("en-US", {timeZone: "America/Denver"});
        $("#parkerTime").append(parkerTime);
        $("#parkerCurrentCond").append(curCond);
        $("#parkerTemp").append(tempInF);
    };
    parkerRequest.send();

    let konaRequest = new XMLHttpRequest();
    konaRequest.open("GET", 'https://api.weather.gov/stations/PHKO/observations/latest', true);
    konaRequest.onload = function(){
        let kdata = JSON.parse(this.response);
        let kCurrentCond = kdata.properties.textDescription;
        let kTempInF = kdata.properties.temperature.value;
        kTempInF = convertTemp(kTempInF);
        let konaTime = new Date(kdata.properties.timestamp).toLocaleString("en-US", {timeZone: "Pacific/Honolulu"});
        $("#konaTime").append(konaTime);
        $("#konaCurrentCond").append(kCurrentCond);
        $("#konaTemp").append(kTempInF);
    };
    //konaRequest.setRequestHeader("User-Agent", "websie / 1.0 just adding Kona weather data to a personal site");
    konaRequest.send();
});