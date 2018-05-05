websocket = new WebSocket("ws://127.0.0.1:8000/client");

websocket.onopen = function(ev) {
	document.getElementById("status").innerHTML = "Connected";

};

websocket.onmessage = function(ev) {
	alert(ev.data)
};

document.getElementById("up").onclick = function() {
 websocket.send(JSON.stringify({
	 action: "move",
	 dir: "up"
 }));
}
document.getElementById("down").onclick = function() {
 websocket.send(JSON.stringify({
	 action: "move",
	 dir: "down"
 }));
}
document.getElementById("left").onclick = function() {
 websocket.send(JSON.stringify({
	 action: "move",
	 dir: "left"
 }));
}
document.getElementById("right").onclick = function() {
 websocket.send(JSON.stringify({
	 action: "move",
	 dir: "right"
 }));
}
