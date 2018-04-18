var five = require('johnny-five');

var board = new five.Board();

board.on('ready', function(){
		var temp = new five.Thermometer({
				comtroller: 'LM35',
				pin: "A0"
		});

		temp.on('change',function(){
				data = this.celsius;
				console.log(data + ' C');

		
		});





});
