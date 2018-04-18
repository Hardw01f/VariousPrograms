var five = require("johnny-five");
 
var board = new five.Board();
var button;
 
board.on("ready", function() {
  // スイッチの設定
  button = new five.Button({
    // デジタル2番ピンにスイッチを接続
    pin: 2,
    // Arduinoに内蔵されているプルアップ回路を有効
    isPullup: true
  });
 
  // スイッチを追加(アクセス許可)
  board.repl.inject({
    button: button
  });
 
  // スイッチを押した
  button.on("down", function() {
    console.log("HIGH");
  });
 
  // スイッチを押し続けて一定時間(初期設定では500ms)経過した
  button.on("hold", function() {
    console.log("HOLD");
  });
 
  // スイッチを離した
  button.on("up", function() {
    console.log("LOW");
  });
});

