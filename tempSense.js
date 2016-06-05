var bs = require('bonescript');
function getTemp() {
	bs.analogRead('P9_40', callback);
}
function callback(data) {
	console.log(data);
}
setTimeout(500,getTemp);
