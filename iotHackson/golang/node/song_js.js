var five = require("johnny-five");
var board = new five.Board({ port: "/dev/cu.usbmodem1421",repl:false});
//var board = new five.Board();

board.on("ready", function() {

  //Piezo音楽始動
  var piezo = new five.Piezo(3);
  //board.repl.inject({
  //  piezo: piezo
  //});
  //play music
  piezo.play({
  song: "C D F D A - A A A A G G G G - - C D F D G - G G G G F F F F - -",
  beats: 1 / 4,
  tempo: 100
  });
  setTimeout(() => {
    process.exit(1);
  }, 5000);
});
