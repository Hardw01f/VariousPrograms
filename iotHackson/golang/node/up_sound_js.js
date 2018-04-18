var five = require("johnny-five");
var board = new five.Board({repl: false});
//var board = new five.Board();

board.on("ready", function() {

  //Servoモーター始動
  console.log("始まり");
  var servo = new five.Servo({
    pin:10
  });

    servo.to(0,500);

  //Piezo音楽始動
  var piezo = new five.Piezo(3);
  //board.repl.inject({
  //  piezo: piezo
  //});

  piezo.play({
  song: "C D F D A - A A A A G G G G - - C D F D G - G G G G F F F F - -",
  beats: 1 / 4,
  tempo: 100
  });
  
  //5秒待って戻す
  setTimeout(() => {
    console.log("終わり");
    servo.to(90,500);
		  setTimeout(() => {
		  process.exit(1);
		  },2000);
  }, 5000);

});
