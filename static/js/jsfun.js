advice_url = "https://api.adviceslip.com/advice"
// perduction_url = "http://sf-pyw.mosyag.in/m04/api/forecasts"
perduction_url = "https://nameless-castle-90009.herokuapp.com/api/forecasts"

$("#ma_head").click(function() {
    $.getJSON(advice_url, function(data){
        advice = data["slip"]["advice"]
        secret_mess (advice);
    });
   
})

function load_predictions() {
    $.getJSON(perduction_url, function(data){
        advice = data["prophecies"]
        update_prediction (advice);
    });
   
}

function update_prediction(paragraphs) {
    {
        $.each(paragraphs, function(i, d) {
          p = $("#p-" + (i + 1) )
          p.html("<p>" + d + "</p>")
        })
      }
}

$("#main_head").click(function() {
    $.getJSON(perduction_url, function(data){
        advice = data["prophecies"]
        update_prediction (advice);
    });
   
})

$(window).bind("load", function() {
//    $.getJSON(perduction_url, function(data){
//        advice = data["prophecies"]
//        update_prediction (advice);
//    });
    var date = new Date();
    $("#main_head").html('<h1>Что день ' + date.getDate() + '.' + (date.getMonth() + 1) + '.' +  date.getFullYear() + ' для Вас готовит!</h1>');
})