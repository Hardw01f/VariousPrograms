//同期的に処理

const execSync = require('child_process').execSync;
const result = execSync('ls -la ./').toString();
console.log(result);
