function image_search() {
  var image_url = $("#image-url-textbox").val();
  $.ajax({
        url : "/image_search/", // the endpoint
        type : "GET", // http method
        data : { image_url: image_url }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            // $('#post-text').val(''); // remove the value from the input
            // console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            var classification_id = json["id"];
            window.location = '/search_result/' + classification_id;
            console.log(json);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function flight_search() {
  $.ajax({
        url : "/flight_search/", // the endpoint
        type : "GET", // http method
        data : { origin: $("#origin").val(),
                 destination: $("#destination").val(),
                 departure_date: $("#departure-date").val(),
                 ret_date: $("#return-date").val()}, // data sent with the post request

        // handle a successful response
        success : function(json) {
            // $('#post-text').val(''); // remove the value from the input
            // console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            console.log(json);
            cheapest = json["results"]["0"];
            $("#notification-text").text("Cheapest flight is by " + cheapest["airline"] + " between " + cheapest["departure_date"] + " and " + cheapest["return_date"] + " for " + cheapest["price"]);
            $("#notification").show();
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

$( "#search-button" ).click(function() {
  image_search();
});

$("#flight-search-button").click(function() {
  flight_search();
})




// function register_sign_in_modal(action) {
//   console.log('went here');
//   if (action == 'register') {
//     $.ajax({
//       url : "static/modal-html/register-modal.html",
//       success : function(result){
//         $("#register-sign-in-modal-header").html('Register');
//         $("#register-sign-in-modal-body").html(result);
//         $("#register-sign-in-modal").modal('show');
//       }
//     });
//   } else {
//     $.ajax({
//       url : "static/modal-html/sign-in-modal.html",
//       success : function(result){
//         $("#register-sign-in-modal-header").html('Sign in');
//         $("#register-sign-in-modal-body").html(result);
//         $("#register-sign-in-modal").modal('show');
//       }
//     });
//   }
// }
