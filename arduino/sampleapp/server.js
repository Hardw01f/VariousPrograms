var five = require('johnny-five');
var board = new five.Board({
    port: "/dev/cu.usbmodem1421"
});

board.on("ready", function() {

    //SERVER
    var html = require("fs").readFileSync("index.html");
    var http = require("http").createServer(function(req, res) {
        res.writeHead(200, {
            "Content-Type": "text/html"
        });
        res.end(html);
    });

    //SOCKET IO
    var io = require("socket.io")(http);
    http.listen(3000);

    var led = new five.Led(13);

    io.on("connection", function(socket) {
        socket.on("msg", function(data) {
            console.log(data);

            var lowered_data = data.toLowerCase();
            console.log(lowered_data)

            if (lowered_data == "on") {
                led.on();
            } else if (lowered_data == "off") {
                led.off();
            } else {
                io.emit("msg", data);
            }
        });
    });
});
