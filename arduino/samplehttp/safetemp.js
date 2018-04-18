var five = require("johnny-five");

var board = new five.Board({
		repl: false
})

board.on("ready", function() {
  var temperature = new five.Thermometer({
    controller: "LM35",
    pin: "A0",
  });

  temperature.on("change", function() {
    console.log(String(this.celsius) + "°C");
	process.exit();
  });
});

