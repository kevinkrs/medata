console.log("Background is runnning")

chrome.browserAction.onClick.addListener(clicked)

function clicked(tab){
  let msg   = {
      txt: "hello"
  } 
    chrome.tabs.sendMessage(tab.id, msg)
}




