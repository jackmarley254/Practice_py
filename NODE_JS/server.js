const http = require('http');
const { createServer } = require('http');
const { hostname } = require('os');

const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World, My name is Jackson an Aspiring Software Engineer!');
});

server.listen(3000, '127.0.0.1', () => {
    console.log('Server running at http://127.0.0.1:3000/');
});
