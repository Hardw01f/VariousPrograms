var five = require("johnny-five"),
  board, motor, led;

board = new five.Board({ port: "/dev/cu.usbmodem1411",repl:false});

board.on("ready", function() {
  // Create a new `motor` hardware instance.
  motor = new five.Motor({
    pin: 5
  });

  // Inject the `motor` hardware into
  // the Repl instance's context;
  // allows direct command line access
  //board.repl.inject({
  //  motor: motor
  //});

  // Motor Event API

  // "start" events fire when the mo tor is started.
  motor.on("start", function() {
    console.log("start", Date.now());

    // Demonstrate motor stop in 2 seconds
    board.wait(6000, function() {
      motor.stop();
    });
  });

  // "stop" events fire when the motor is stopped.
  motor.on("stop", function() {
    console.log("stop", Date.now());
  });

  // Motor API

  // start([speed)
  // Start the motor. `isOn` property set to |true|
  // Takes an optional parameter `speed` [0-255]
  // to define the motor speed if a PWM Pin is
  // used to connect the motor.
  motor.start();
  setTimeout(() => {
    process.exit(1);
  }, 7000);
  // stop()
  // Stop the motor. `isOn` property set to |false|
});
