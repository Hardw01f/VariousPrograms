var five = require("johnny-five");


five.Board().on("ready", function() {

  // Initialize the RGB LED
  var led = new five.Led.RGB({
    pins: {
      red: 6,
      green: 5,
      blue: 3
    }
  });

  // RGB LED alternate constructor
  // This will normalize an array of pins in [r, g, b]
  // order to an object (like above) that's shaped like:
  // {
  //   red: r,
  //   green: g,
  //   blue: b
  // }
  //var led = new five.Led.RGB([3,5,6]);

  // Add led to REPL (optional)
  //this.repl.inject({
  //  led: led
  //});

  // Turn it on and set the initial color
  var index = 0;
  var rainbow = ["FF0000", "FF7F00", "FFFF00", "00FF00", "0000FF", "4B0082", "8F00FF"];

  //led.on();
  this.loop(1000,function(){
  led.color(rainbow[index++]);
  if(index === rainbow.length){
  		  index = 0;
  }
  });
  //led.blink(1000)

  //led.on();
  //led.color("#0000cc");

  //led.blink(1000);

});

