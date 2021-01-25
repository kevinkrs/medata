console.log("Hello from the content-script")


var count = document.querySelectorAll('.issue-item__title').length;
var links = []

for (var i = 0; i < count; i++) {
    var link = document.querySelectorAll('.issue-item__title')[i].innerHTML
    links.push(link)
}

console.log(links)


browser.runtime.onMessage.addListener(function(msg, sender, response){
    if ((msg.from === "binder")&&(msg.subject === "getLinks")) {
        response(links)
    
    }
    else{
        response ({}) 
    }
})