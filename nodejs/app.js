var io = require('socket.io').listen(8008);
var querystring = require('querystring');
var http = require('http');

io.sockets.on('connection', function(socket){
	socket.on('nuevo comentario', function(data){
		var values = querystring.stringify(data);
		var options = {
			hostname: 'localhost',
			port: '8000',
			path: '/nuevo_comentario/',
			method: 'POST',
			headers: {
				'Content-Type': 'x-www-form-urlencoded',
				'Content-Length': values.length
			}
		};
		var req = http.request(options, function(res){
			res.setEncoding('utf8');
			res.on('data', function(data){
				io.sockets.emit('comentario nuevo', data);
			});
		});
		req.write(values);
		req.end();
	});
});