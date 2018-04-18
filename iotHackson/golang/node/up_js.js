var five = require("johnny-five");
var board = new five.Board({ port: "/dev/cu.usbmodem1421",repl: false});
//var board = new five.Board();

board.on("ready", function() {

  //Servoモーター始動
  var servo = new five.Servo({
    pin:10
  });
  //up motor
  servo.to(0,500);
  setTimeout(() => {
    process.exit(1);
  }, 2000);

});
