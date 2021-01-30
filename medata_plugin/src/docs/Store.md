## Classes

<dl>
<dt><a href="#state">state</a></dt>
<dd></dd>
<dt><a href="#mutations">mutations</a></dt>
<dd></dd>
<dt><a href="#actions">actions</a></dt>
<dd></dd>
</dl>

<a name="state"></a>

## state
**Kind**: global class  

* [state](#state)
    * [.metadata](#state.metadata)
    * [.query](#state.query)
    * [.currentIn](#state.currentIn)
    * [.currentInID](#state.currentInID)
    * [.currentCategories](#state.currentCategories)
    * [.currentAnswer](#state.currentAnswer)
    * [.answerUpvoteBool](#state.answerUpvoteBool)
    * [.currentUserInput](#state.currentUserInput)
    * [.insightVoteBool](#state.insightVoteBool)
    * [.autocomplete](#state.autocomplete)
    * [.binder](#state.binder)

<a name="state.metadata"></a>

### state.metadata
Array for saving recieved backend data and access it in every other vue component.

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.query"></a>

### state.query
Current user URL.

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.currentIn"></a>

### state.currentIn
Current selected insight name.

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.currentInID"></a>

### state.currentInID
Current selected insight ID.

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.currentCategories"></a>

### state.currentCategories
Current CSS categories of visited article.

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.currentAnswer"></a>

### state.currentAnswer
Selected answer by user (yellow-status).

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.answerUpvoteBool"></a>

### state.answerUpvoteBool
Parameter for backend api request.

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.currentUserInput"></a>

### state.currentUserInput
Current user input (new insight answer or new insigt).

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.insightVoteBool"></a>

### state.insightVoteBool
Parameter for backend api request.

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.autocomplete"></a>

### state.autocomplete
Array for saving recieved topic related keywords for autocomplete feature in the _Home.vue_ component.

**Kind**: static property of [<code>state</code>](#state)  
<a name="state.binder"></a>

### state.binder
Array of URL's from binder to request data from backend and trigger direct-download with all the available insight data.

**Kind**: static property of [<code>state</code>](#state)  
<a name="mutations"></a>

## mutations
**Kind**: global class  

* [mutations](#mutations)
    * [.setMetadata(state, payload)](#mutations.setMetadata)
    * [.setQuery(state, payload)](#mutations.setQuery)
    * [.setCurrentInName(state, payload)](#mutations.setCurrentInName)
    * [.setcurrentInID(state, payload)](#mutations.setcurrentInID)
    * [.setCurrentAnswer(payload)](#mutations.setCurrentAnswer)
    * [.setUserInput(state, payload)](#mutations.setUserInput)
    * [.setAutocomplete(state, payload)](#mutations.setAutocomplete)
    * [.setBinder(state, payload)](#mutations.setBinder)

<a name="mutations.setMetadata"></a>

### mutations.setMetadata(state, payload)
Sets the data recieved from the backend into a state.metadata property in order to be able to access it in other components.

**Kind**: static method of [<code>mutations</code>](#mutations)  

| Param | Type |
| --- | --- |
| state | <code>array</code> | 
| payload | <code>array</code> | 

<a name="mutations.setQuery"></a>

### mutations.setQuery(state, payload)
Sets current URL from dl.acm.org that user is visiting when opening the plugin to the state.query property.

**Kind**: static method of [<code>mutations</code>](#mutations)  

| Param | Type |
| --- | --- |
| state | <code>String</code> | 
| payload | <code>String</code> | 

<a name="mutations.setCurrentInName"></a>

### mutations.setCurrentInName(state, payload)
Sets by user selected (unfolded) insight name to the state.currentIn property.

**Kind**: static method of [<code>mutations</code>](#mutations)  

| Param | Type |
| --- | --- |
| state | <code>String</code> | 
| payload | <code>String</code> | 

<a name="mutations.setcurrentInID"></a>

### mutations.setcurrentInID(state, payload)
Sets by user selected (unfolded) insight ID to the state.currentInID property.

**Kind**: static method of [<code>mutations</code>](#mutations)  

| Param | Type |
| --- | --- |
| state | <code>String</code> | 
| payload | <code>String</code> | 

<a name="mutations.setCurrentAnswer"></a>

### mutations.setCurrentAnswer(payload)
Sets user selected insight answer (yellow-status) to the state.currentAnswer property.

**Kind**: static method of [<code>mutations</code>](#mutations)  

| Param | Type |
| --- | --- |
| payload | <code>String</code> | 

<a name="mutations.setUserInput"></a>

### mutations.setUserInput(state, payload)
Sets user input for submitting either a new insight answer or a completely new insight to the state.currentUserInput property.

**Kind**: static method of [<code>mutations</code>](#mutations)  

| Param | Type |
| --- | --- |
| state | <code>String</code> | 
| payload | <code>String</code> | 

<a name="mutations.setAutocomplete"></a>

### mutations.setAutocomplete(state, payload)
Saves the recieved keyword array for the autocomplete feature into a stat.autocomplete property.

**Kind**: static method of [<code>mutations</code>](#mutations)  

| Param | Type |
| --- | --- |
| state | <code>Array</code> | 
| payload | <code>Array</code> | 

<a name="mutations.setBinder"></a>

### mutations.setBinder(state, payload)
Saves scraped URL's of users Binder entries to a state.binder property.

**Kind**: static method of [<code>mutations</code>](#mutations)  

| Param | Type |
| --- | --- |
| state | <code>Array</code> | 
| payload | <code>Array</code> | 

<a name="actions"></a>

## actions
**Kind**: global class  

* [actions](#actions)
    * [.loadQuery(payload)](#actions.loadQuery)
    * [.loadMetadata()](#actions.loadMetadata)
    * [.loadFurtherInformation()](#actions.loadFurtherInformation)
    * [.loadAutocomplete()](#actions.loadAutocomplete)
    * [.loadDownload()](#actions.loadDownload)
    * [.fetchUserInput(payload)](#actions.fetchUserInput)
    * [.fetchUserAnswer(payload)](#actions.fetchUserAnswer)
    * [.fetchInName(payload)](#actions.fetchInName)
    * [.fetchBinder(payload)](#actions.fetchBinder)
    * [.sendAnswer()](#actions.sendAnswer)
    * [.sendRateAnswer()](#actions.sendRateAnswer)
    * [.sendInsight()](#actions.sendInsight)
    * [.sendRateRelevanceInsight()](#actions.sendRateRelevanceInsight)
    * [.sendInsightNotRelevantError()](#actions.sendInsightNotRelevantError)
    * [.sendValueError()](#actions.sendValueError)
    * [.sendTypoError()](#actions.sendTypoError)
    * [.sendBinder()](#actions.sendBinder)

<a name="actions.loadQuery"></a>

### actions.loadQuery(payload)
Triggers _mutation_ to save current tab URL if it is valid.

**Kind**: static method of [<code>actions</code>](#actions)  

| Param | Type |
| --- | --- |
| payload | <code>String</code> | 

<a name="actions.loadMetadata"></a>

### actions.loadMetadata()
Sends api call to backend in order to recieve available metadata and then passing it to the the fitting _mutation_.

**Kind**: static method of [<code>actions</code>](#actions)  
<a name="actions.loadFurtherInformation"></a>

### actions.loadFurtherInformation()
Sends a request to the backend for further information. Backend starts scraper on the forwarded current user URL.

**Kind**: static method of [<code>actions</code>](#actions)  
<a name="actions.loadAutocomplete"></a>

### actions.loadAutocomplete()
Sends api call to backend to recieve topic related keywords for the autocomplete function and passing it then to the fitting _mutation_.

**Kind**: static method of [<code>actions</code>](#actions)  
<a name="actions.loadDownload"></a>

### actions.loadDownload()
Requests data for the current article or paper and starts a direct download once recieved.

**Kind**: static method of [<code>actions</code>](#actions)  
<a name="actions.fetchUserInput"></a>

### actions.fetchUserInput(payload)
Payload is forwarded to _mutation_ to save it into the state.currentUserInput property.

**Kind**: static method of [<code>actions</code>](#actions)  

| Param | Type |
| --- | --- |
| payload | <code>String</code> | 

<a name="actions.fetchUserAnswer"></a>

### actions.fetchUserAnswer(payload)
Selected user answer is forwarded to _mutation_ to save it into the state.currentAnswer property.

**Kind**: static method of [<code>actions</code>](#actions)  

| Param | Type |
| --- | --- |
| payload | <code>String</code> | 

<a name="actions.fetchInName"></a>

### actions.fetchInName(payload)
Current unfolded insight name is forwarder to _mutation_ to save it into the state.currentInName property.

**Kind**: static method of [<code>actions</code>](#actions)  

| Param | Type |
| --- | --- |
| payload | <code>String</code> | 

<a name="actions.fetchBinder"></a>

### actions.fetchBinder(payload)
Scraped Binder URL's are forwarded to _mutation_ to save them into the state.binder property.

**Kind**: static method of [<code>actions</code>](#actions)  

| Param | Type |
| --- | --- |
| payload | <code>Array</code> | 

<a name="actions.sendAnswer"></a>

### actions.sendAnswer()
Calls function that sends api call to backend for posting a new insight answer (yellow or red-status).

**Kind**: static method of [<code>actions</code>](#actions)  
<a name="actions.sendRateAnswer"></a>

### actions.sendRateAnswer()
Calls function that sends api call to backend for rating an insight answer (green or yellow-status).

**Kind**: static method of [<code>actions</code>](#actions)  
<a name="actions.sendInsight"></a>

### actions.sendInsight()
Calls function that sends api call to backend for posting a new insight.

**Kind**: static method of [<code>actions</code>](#actions)  
<a name="actions.sendRateRelevanceInsight"></a>

### actions.sendRateRelevanceInsight()
Calls function that sends api call to backend to upvote insight relevance when unfolding any insight.

**Kind**: static method of [<code>actions</code>](#actions)  
<a name="actions.sendInsightNotRelevantError"></a>

### actions.sendInsightNotRelevantError()
Calls function that sends api call to backend for posting an insight-not-relevant-error (equals double downvote).

**Kind**: static method of [<code>actions</code>](#actions)  
<a name="actions.sendValueError"></a>

### actions.sendValueError()
Calls function that sends api call to backend for posting a value-error.

**Kind**: static method of [<code>actions</code>](#actions)  
<a name="actions.sendTypoError"></a>

### actions.sendTypoError()
Calls function that sends api call to backend for posting a type-error.

**Kind**: static method of [<code>actions</code>](#actions)  
<a name="actions.sendBinder"></a>

### actions.sendBinder()
Calls function that sends api call to backend forwarding the state.binder array with all Binder URL's and starts direct-downlaod of the csv file after recieving data.

**Kind**: static method of [<code>actions</code>](#actions) 