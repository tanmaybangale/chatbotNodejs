try{

var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
  console.log('a user connected');
  
  socket.on('chat message', function(msg){
    console.log('message: ' + msg);
    
    io.emit('userinput',msg +"@" +socket.id  );		
    
  });

  socket.on('response_generated' ,function(msg){
    resp = msg.split("@");
    
    io.to(resp[1]).emit('chat message',resp[0]);
    
  });

  socket.on('disconnect', function(){
    console.log('user disconnected');
  });

});

http.listen(3000, function(){
  console.log('listening on *:3000');
});

}
catch(err)
{
console.log(err);
}
