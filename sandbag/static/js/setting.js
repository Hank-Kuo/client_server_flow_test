// Date time for type and version
$('#datetimepicker1').datetimepicker({
    defaultDate: new Date(),
    format: 'DD/MM/YYYY H:mm',
    sideBySide: true
});
$('#datetimepicker2').datetimepicker({
    defaultDate: new Date(),
    format: 'DD/MM/YYYY H:mm',
    sideBySide: true
});




var inputValue = 1
var inputStep = 1
// Token button 
$("#submit-token").click(function(){
  Swal.fire({
    title: 'Create Token',
    html: `<input type="number" value="${inputValue}" step="${inputStep}" class="swal2-input" id="swal2-range-value">`,
    input: 'range',
    customClass: 'swal-height',
    inputValue,
    inputAttributes: {
      min: 0,
      max: 100,
      step: inputStep
    },
      onOpen: () => {
      const inputRange = Swal.getInput()
      const inputNumber = Swal.getContent().querySelector('#swal2-range-value')
      const button = Swal.getActions();
      inputRange.addEventListener ('input', () => {
        inputNumber.value=inputRange.value;
      });
      inputNumber.addEventListener ('change', () => {
        inputRange.value=inputNumber.value;
        inputRange.nextElementSibling.value=inputNumber.value;
      });
      button.addEventListener('click',()=>{
        console.log(inputNumber.value);
        $.ajax({
            url: "/ajax_token",
            type: 'POST',
            data: { "token":inputNumber.value,
            },
            dataType: 'json',
            success: function(data) {
                console.log("success")   
            }
            });
      });
    }
  })
});

$('#check-token').on('click',function(){
  //if() not disabled can do....
  var link = document.createElement("a");
  link.href = '/token';
  link.style = "visibility:hidden";
  link.target = "_blank";
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link); 
});