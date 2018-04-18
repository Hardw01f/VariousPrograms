var fs = require("fs");
var http = require("http");
var server = http.createServer();

var five = require("johnny-five");

five.Board().on("ready", function() {

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

  var temperature = new five.Thermometer({
    controller: "LM35",
    pin: "A0"
  });

  temperature.on("change", function() {
    console.log(this.celsius + "°C", this.fahrenheit + "°F");
  });

  // Control
  io.on("connection", function(socket) {
    socket.on("msg", function(celsius) {
      console.log(celsius);
    });
  });


});

