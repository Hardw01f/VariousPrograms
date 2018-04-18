const exec = require('child_process').exec;

exec('ls -la ./',(err,stdout, stderr) => {
    if(err){ console.log(err);}
    console.log(stdout);
});
