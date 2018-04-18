const exec = require('child_process').exec;

var five = require("johnny-five");
var board;
var sensor;
var count;
 
board = new five.Board();
 
board.on("ready", function() {
	// Sensor
	sensor = new five.Sensor({
		// アナログ0番ピン
		pin: "A0",
		// 100ms間隔でセンサーにアクセスする 初期設定では25ms
		freq: 5
	    });
 
	// センサーを追加(アクセス許可)
	board.repl.inject({
		pot: sensor
		    });

	// センサーの入力値を0～100にスケーリングして取得
	sensor.scale(0, 100).on("data", function() {
		// console.log(this.value);
	    });
 
	// センサーの入力値が範囲内(40～100)になった
	sensor.within([10, 100], function() {
		// console.log("近！");
		count += 1;
	    });

    });

  setInterval(function() {
	   // console.log(count);
	 if(count >= 50 ){
//		console.log("イノシシ!!!")
	now = getNow();

	// console.log('.client '+ now);

 	exec('./client ' +now,(err,stdout, stderr) => {
   	if(err){ console.log(err);}
     	console.log(stdout);
 		});
 	now = getNow();
	exec('python line.py ' +now,(err,stdout, stderr) => {
   	if(err){ console.log(err);}
     	console.log(stdout);
 		});

	 }
	  count = 0;
  }, 1000);

function getNow() {
	var date=new Date();
	var year = date.getFullYear();
	var month = date.getMonth()+1;
	//var week = date.getDay();
	var day = date.getDate();
	var hours = date.getHours();
  	var minutes = date.getMinutes();	

	var now = year + '-' + month + '-' + day + '-' + hours + '-' + minutes + ',B' ; 	
	return now;
//	console.log(now);
}
