$(document).ready(function(){
    var socket = io.connect("http://127.0.0.1:5000")

    socket.on('connect', function(){
        console.log("I am here!")
    })
    socket.on("message", function(msg){
    $("#numbers").append(msg)
    })

    $("#counter").on("click", function(){
     socket.send(Number($("#numbers").val()))
     })
})