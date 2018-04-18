var five = require('johnny-five');
var board = new five.Board();

board.on("ready",function(){


    var piano = new five.Piezo(13);

    piano.play({
        song: [
            ["C4", 1/4],
            ["D4", 1/2],
            [null,1],
            ["F4",1]
        ],
        tempo: 100
    });
});