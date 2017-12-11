function updateTemp() {
    $.getJSON('/temp', function(data){
    $("#temp").text = response.temp;
     })
}

setInterval('updateTemp()',1000*60)
setInterval(console.log("logging..."),1000*60)