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
	sensor.scale(0, 300).on("data", function() {
		// console.log(this.value);
	    });
 
	// センサーの入力値が範囲内(40～100)になった
	sensor.within([40, 300], function() {
		// console.log("近！");
		count += 1;
	    });

    });

  setInterval(function() {
	   // console.log(count);
	 if(count >= 10 ){
		console.log("イノシシ!!!")

		exec('ls -la ./',(err,stdout, stderr) => {
    	if(err){ console.log(err);}
    	console.log(stdout);
		});

	 }
	  count = 0;
  }, 1000);
