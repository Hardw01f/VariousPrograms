
var five = require("johnny-five");
var board = new five.Board();

board.on("ready", function() {

  var servo = new five.Servo({
        pin:10,
        range:[0,110],
        value: 90,
        interval: 10,
        center: true 
  });

  // Sweep from 0-180 and repeat.
  servo.sweep()
});
