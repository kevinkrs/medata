browser.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  console.log("Background Script is running")
  chrome.tabs.executeScript({
    file: 'js/content-script.js',
  })
})
