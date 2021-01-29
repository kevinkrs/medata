console.log("Hello from the content-script")


/**
 * Scraping all elements by className
 *
 */
var count = document.querySelectorAll('.issue-item__title').length;
var links = []

/**
 * Adding each element to the array _links_
 */
for (var i = 0; i < count; i++) {
    var link = document.querySelectorAll('.issue-item__title')[i].innerHTML
    links.push(link)
}

console.log(links)

/**
 * Listener for plugin-to-content-script communication. Awaiting a _sender_ and a _subject_.
 * Responding with the _links_ array.
 */
browser.runtime.onMessage.addListener(function(msg, sender, response){
    if ((msg.from === "binder")&&(msg.subject === "getLinks")) {
        response(links)
    
    }
    else{
        response ({}) 
    }
})