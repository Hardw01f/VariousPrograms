'use strict';

const io = require('socket.io-client');
const socket = io('localhost:3000');

socket.on('connect', () => {
    socket.emit("message", 'send message.');

    socket.on('chat message', (msg) => {
        // io.emit('chat message', msg);
        console.log(`message: ${msg}`);
    });
});