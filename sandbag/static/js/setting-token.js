var $TABLE = $('#table');
var $BTN = $('#export-btn');
var $EXPORT = $('#export');

window.onload = function()  {
  var socket = new WebSocket("ws:" + window.location.host +"/ws_setting_token/");
  var id =0;
  dic={}
  var flag = true;
      socket.onopen = function (e) {
          console.log('WebSocket open');
      };
      socket.onmessage = function (e) {
          var data = JSON.parse(e.data);
          var key = Object.keys(data);
          //create data first 
          if(flag){
            for(; id<key.length ; id++){
              var isValid = data[key[id]][0];
              var username = data[key[id]][1];
              var token = key[id]
              createTd(id,username,token,isValid);
            } 
            flag=false;
            dic=data;
          }
          // add and update 
          if(JSON.stringify(dic) != JSON.stringify(data)){
            if(Object.keys(dic).length < Object.keys(data).length){
              console.log("add");
              add(id,dic,data);
              id+=1;
            }else{
              update(data);
              console.log("update")
            }   
            dic=data;
          };
      };
      socket.onclose=function(e){      
          socket.close(); 
      };
}

var createTd = function(id,username,token,isValid){
    $('#table tr:last').after('<tr><td> <p id=id-'+username+'>'+id+'</p></td>\
    <td> <p id=username-'+token+'>'+username+'</p></td>\
    <td> <p id=token-'+token+'>'+token+'</p></td>\
    <td> <p id=isValid-'+token+'>'+isValid+'</p> </td> </tr>');
}

var update =function(data){
  var key = Object.keys(data);          
  for(var count=0; count<key.length ; count++){
    var isValid = data[key[count]][0];
    var username = data[key[count]][1];
    var token = key[count];
    console.log(isValid);
    $('#username-'+token).html(username);
    $('#token-'+token).html(token);
    $('#isValid-'+token).html(isValid.toString());
  } 
}

var add = function(id,dic,data){
  var newKey = Object.keys(data); 
  var oldKey = Object.keys(dic);
  for(var i=0; i<newKey.length ; i++){
    var username = data[newKey[i]][1];
    var token = newKey[i];
    var isValid = data[newKey[i]][0];
    var check = oldKey.indexOf(token);
    if(check==-1){
      createTd(id,username,token,isValid);
    }
    

  }
  


}




/*
$('.table-add').click(function() {
  $('#table tr:last').after('<tr><td></td></tr><tr>...</tr>');
});
$('.table-remove').click(function() {
  $(this).parents('tr').detach();
});
$('.table-up').click(function() {
  var $row = $(this).parents('tr');
  if ($row.index() === 1) return; // Don't go above the header
  $row.prev().before($row.get(0));
});

$('.table-down').click(function() {
  var $row = $(this).parents('tr');
  $row.next().after($row.get(0));
});
*/
// A few jQuery helpers for exporting only
//jQuery.fn.pop = [].pop;
//jQuery.fn.shiftunique = [].shift;
/*
$BTN.click(function() {
  var $rows = $TABLE.find('tr:not(:hidden)');
  var headers = [];
  var data = [];

  // Get the headers (add special header logic here)
  $($rows.shift()).find('th:not(:empty):not([data-attr-ignore])').each(function() {
    headers.push($(this).text().toLowerCase());
  });

  // Turn all existing rows into a loopable array
  $rows.each(function() {
    var $td = $(this).find('td');
    var h = {};

    // Use the headers from earlier to name our hash keys
    headers.forEach(function(header, i) {
      h[header] = $td.eq(i).text(); // will adapt for inputs if text is empty
      
    });
    data.push(h);
    console.log(data)
  });

  // Output the result
  $EXPORT.text(JSON.stringify(data));
});


*/