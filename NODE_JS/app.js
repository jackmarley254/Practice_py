console.log('Hello World!');

const fs = require('fs');
//const http = require('http');
fs.readFile('example.txt', 'utf8', (err, data) => {
		if (err) {
			console.error(err);
			return;
		}
		console.log(data);
});

//console.log(process.argv);
