console.log("Hello World");

var btn = document.getElementById("btn");
btn.addEventListener("click", function() {

var price = "50000";
var id = "92345";
var describe =  "Items price";


var myHeaders = new Headers();
myHeaders.append("x-ApiKey", "TEST_API_KEY");
myHeaders.append("content-type", "application/json");


var raw_new = {    "callBackUrl": "https://www.taeillo.com",   "reference": id,    "merchantId": "117143",   "description": describe,   "amount": price};

var raw = JSON.stringify(raw_new)

var requestOptions = {
method: 'POST',
headers: myHeaders,
body: raw,
redirect: 'follow'
};

var url;

fetch("https://paywithspectaapi.sterling.ng/api/Purchase/CreatePaymentUrl", requestOptions)
.then(response => response.json())
.then(result => url = result)
.then(() => window.location.replace(url.result))
.catch(error => console.log('error', error));



//Do something here

}, false);






