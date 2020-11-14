// Button click 
$("#sandbag_btn_submit").click(function(){
    var endpoint = $("#sandbag_endpoint").val();
    swal("Set up your Endpoint", "", "success");
    $.ajax({
        url: "/ajax_sandept",
        type: 'POST',
        data: { endpoint:JSON.stringify(endpoint)
        },
        dataType: 'json',
        success: function(data) {
            $('#sandept_result').html(data.result);
        }
    });
 });

 $("#sandbag_btn_reset").click(function(){
    swal("Reset your Endpoint", "", "success");
    $.ajax({
        url: "/ajax_sandept",
        type: 'POST',
        data: { endpoint:JSON.stringify()
        },
        dataType: 'json',
        success: function(data) {
            $('#sandept_result').html(data.result);
            document.getElementById("sandbag_endpoint").value = data.result;
           
        }
        });
 });

 $("#translate_btn_submit").click(function(){
    var endpoint = $("#translate_endpoint").val();
    console.log(endpoint)
    swal("Set up your Endpoint", "", "success");
    $.ajax({
        url: "/ajax_translept",
        type: 'POST',
        data: { endpoint:JSON.stringify(endpoint)
        },
        dataType: 'json',
        success: function(data) {
            console.log(data["result"])
            $('#translate_result').html(data["result"]);
        }
        });
 });

 $("#translate_btn_reset").click(function(){
    swal("Reset your Endpoint", "", "success");
    $.ajax({
        url: "/ajax_translept",
        type: 'POST',
        data: { endpoint:JSON.stringify()
        },
        dataType: 'json',
        success: function(data) {
            $('#sandept_result').html(data.result);
            document.getElementById("sandbag_endpoint").value = data.result;
           
        }
        });
 });

// Get rank from all user  
var getrank = function(data){
    var rank = "";
    data+=1
    if(data==1){
        rank = data+" st"
    }else if (data==2){
        rank = data+" nd"
    }else if (data==2){
        rank = data+" td"
    }else{
        rank = data+" th"
    }
    return rank ;
} 

// Get user trankslate API information 
var translateApiInfo =function(ans){
    var response = "success"
    if(ans=="false"){
        response = "error"
    }
    $("#translate_api_info").click(function(){
        swal("Translate API ", "", response);
    }); 
} 
var errorArr =["","",""] 
$(function(){
    $.getJSON("/sandscore", // Your AJAX route here
     function(data) {
        $('#sandscr_result').html(data["score"]);
        console.log(data)
        $('#sanderr_result_3').html(errorArr[0]);
        $('#sanderr_result_2').html(errorArr[1]);
        $('#sanderr_result_1').html(errorArr[2]);
        errorArr.push(data["error"])
                if(errorArr.length >=3){
                    errorArr.shift();
                }
                $('#sand_rank').html('1 st'); 

                translateApiInfo(data["translate_api"])
     }
    );
    setTimeout(arguments.callee, 1000);
   })();
// websocket 
/* 
window.onload = function()  {
        var socket = new WebSocket("ws:" + window.location.host +"/ws_sand/");
        var errorArr =["","",""] 
            socket.onopen = function (e) {
                console.log('WebSocket open');
            };
            socket.onmessage = function (e) {
                var data = JSON.parse(e.data);
                $('#sandscr_result').html(data["score"]);
                console.log(data)
                $('#sanderr_result_3').html(errorArr[0]);
                $('#sanderr_result_2').html(errorArr[1]);
                $('#sanderr_result_1').html(errorArr[2]);
                errorArr.push(data["error"])
                if(errorArr.length >=3){
                    errorArr.shift();
                }
                $('#sand_rank').html('1 st'); 

                translateApiInfo(data["translate_api"])

            };
            socket.onclose=function(e){
                alert("Connection closed!");
                socket.close(); 
            };
}
*/
