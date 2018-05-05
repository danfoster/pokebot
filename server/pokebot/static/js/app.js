websocket = new WebSocket("ws://127.0.0.1:8000/client");

websocket.onopen = function(ev) {
	document.getElementById("status").innerHTML = "Connected";
	websocket.send("foo");

};

websocket.onmessage = function(ev) {
	alert(ev.data)
};

document.getElementById("button").onclick = function() {
 websocket.send("bar");
}
