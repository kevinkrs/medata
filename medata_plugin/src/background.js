
/**
 * This javascript code is responsible for the ommunication between the plugin and the whole browser application.
 * It can access for example browser tabs and a bunch of other browser related actions.
 *
 */
browser.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  console.log("Background Script is running")
  chrome.tabs.executeScript({
    file: 'js/content-script.js',
  })
})