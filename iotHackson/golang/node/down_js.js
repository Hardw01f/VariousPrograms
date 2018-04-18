var five = require("johnny-five");
var board = new five.Board({ port: "/dev/cu.usbmodem1421",repl:false});
//var board = new five.Board();

board.on("ready", function() {
    //Servoモーター始動
    var servo = new five.Servo({
        pin:10
    });
    //down motor 
    servo.to(90,500);
    setTimeout(() => {
        process.exit(1);
      }, 2000);

});