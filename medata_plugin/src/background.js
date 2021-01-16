browser.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  alert('Hello from the background')
})


