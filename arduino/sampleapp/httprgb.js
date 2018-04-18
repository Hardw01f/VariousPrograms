var fs = require("fs");
var http = require("http");
var server = http.createServer();

var five = require("johnny-five");
var board = new five.Board();

board.on("ready", function() {
  // Server
  server.on("request", function(req, res) {
    var stream = fs.createReadStream("index.html");
    res.writeHead(200, {
      "Content-Type": "text/html"
    });
    stream.pipe(res);
  });

  // Socket.IO
  var io = require("socket.io").listen(server);
  server.listen(8080);

  // LED
  var led = new five.Led.RGB({
    pins: {
      red: 6,
      green: 5,
      blue: 3
    }
  });

  // Control
  io.on("connection", function(socket) {
    socket.on("msg", function(color) {
      console.log(color);
	
      if (color == "off") {
        led.off();
	  } else {
        led.color(color);
      }
    });
  });
});
