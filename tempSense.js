var bs = require('bonescript');
function getTemp() {
	bs.analogRead('P9_40', callback);
}
var temp;
function callback(data) {
	temp = ((data / 100)*1.8)
	console.log(temp);
}
setTimeout(getTemp,500);
