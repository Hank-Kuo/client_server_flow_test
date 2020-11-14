
window.onload = function()  {
  var socket = new WebSocket("ws:" + window.location.host +"/ws_sand_chart/");
  chart=[];
  user=[];
  socket.onopen = function (e) {
      console.log('WebSocket open');
  };
  socket.onmessage = function (e) {
    var data = JSON.parse(e.data);
    var dataScore = data["score"];
    var total = Object.keys(dataScore).length;
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

    for(var i =0 ; i < total ; i++){
      if(!user.includes(Object.keys(dataScore)[i])){
        user.push(Object.keys(dataScore)[i]);
        createDiv(i,user[i],data["translate_api"][user[i]])
        chart.push(createChart(i));
      }
    }
    //update the chart 
    update(user,dataScore,chart,time);
  };
  socket.onclose=function(e){  
      alert("Connection closed!");
      socket.close(); 
  };
}

var createDiv = function(number,name,translate_api){
    var objTo = document.getElementById('element1');
    var div1=document.createElement("div"); 
    var div2=document.createElement("div"); 
    var div3=document.createElement("div"); 
    var h = document.createElement("h3");
    var btn = document.createElement("BUTTON");  
    var con=document.createElement("canvas"); 
    div1.className = "col-lg-6" ;
    div2.className = "au-card m-b-30" ;
    div3.className = "au-card-inner" ;
    h.className = "title-2 m-b-40";
    btn.innerHTML=name;
    btn.id=name;
    btn.addEventListener("click", function(e) {
      showQuest(name,translate_api);
    });
    con.id = "Chart"+number;
    con.setAttribute("style", "margin:30px -10px");
    objTo.appendChild(div1);
    div1.appendChild(div2);
    div2.appendChild(div3);
    div3.appendChild(h);
    h.appendChild(btn);
    h.appendChild(con);
}

var createChart = function(number){
      var ctx = document.getElementById("Chart"+number);
      if (ctx) {
        ctx.height = 150;
        var myChart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: ["2010", "2011", "2012", "2013", "2014", "2015", "2016"],
            type: 'line',
            defaultFontFamily: 'Poppins',
            datasets: [{
              data: [1, 7, 3, 5, 2, 10, 7],
              label: "Expense",
              backgroundColor: 'rgba(0,103,255,.15)',
              borderColor: 'rgba(0,103,255,0.5)',
              borderWidth: 3.5,
              pointStyle: 'circle',
              pointRadius: 5,
              pointBorderColor: 'transparent',
              pointBackgroundColor: 'rgba(0,103,255,0.5)',
            },]
          },
          options: {
            responsive: true,
            tooltips: {
              mode: 'index',
              titleFontSize: 12,
              titleFontColor: '#000',
              bodyFontColor: '#000',
              backgroundColor: '#fff',
              titleFontFamily: 'Poppins',
              bodyFontFamily: 'Poppins',
              cornerRadius: 3,
              intersect: false,
            },
            legend: {
              display: false,
              position: 'top',
              labels: {
                usePointStyle: true,
                fontFamily: 'Poppins',
              },
            },
            scales: {
              xAxes: [{
                display: true,
                gridLines: {
                  display: false,
                  drawBorder: false
                },
                scaleLabel: {
                  display: false,
                  labelString: 'Month'
                },
                ticks: {
                  fontFamily: "Poppins"
                }
              }],
              yAxes: [{
                display: true,
                gridLines: {
                  display: false,
                  drawBorder: false
                },
                scaleLabel: {
                  display: true,
                  fontFamily: "Poppins"
                },
                ticks: {
                  fontFamily: "Poppins"
                }
              }]
            },
            title: {
              display: false,
            }
          }
        });   
        return myChart;
        
      }
      
}

// Update chart 
var update = function(user,dataScore,chart,time){
  console.log(user)
  for(var i =0;i<chart.length;i++){
    chart[i].data.datasets[0].data.shift();
    chart[i].data.labels.shift();
    chart[i].data.labels.push(time);
    score = dataScore[user[i]];
    chart[i].data.datasets[0].data.push(score);
    chart[i].update();
  }
}

// show 
var showQuest = function(name,translate_api) { 
  var color ="<font color='green'>"
  if(translate_api=="false"){
    color = "<font color='red'>"
  }
  swal({title: name,html: '<b >translate API : '+color+translate_api+'</font></b>'});
};

