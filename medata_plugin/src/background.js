browser.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  alert('Hello from the background')
})

console.log("Background is runnning")

window.addEventListener('load', function (evt) {
  chrome.extension.getBackgroundPage().chrome.tabs.executeScript(null, {
      file: 'Binder.vue'
  });;
});


chrome.runtime.onMessage.addListener(function (message) {
  document.getElementById('json-content').innerHTML = message;
});


