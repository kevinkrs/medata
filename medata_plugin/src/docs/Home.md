# main

The core component of the plugin. All the interaction between user an programm
happens here.

## Data

| Name            | Type      | Description                                                                                                  | Initial value |
| --------------- | --------- | ------------------------------------------------------------------------------------------------------------ | ------------- |
| `userInput`     | `string`  | Empty strings for saving user input inside given input fields                                                | `""`          |
| `legendVisible` | `boolean` | Trigger for collapsing information box                                                                       | `false`       |
| `filtered`      | `array`   | Saves recieved array of topic related words from backend. Required for the _add insight_ autocomplete option | `[]`          |
| `modal`         | `boolean` | Property for the autocomplete option                                                                         | `false`       |

## Methods

### openGit()

Click function for top right git icon to open github repository

**Syntax**

```typescript
openGit(): void
```

### filterParameters()

Autocomplete function using the _filtered_ property from _data_ which is fed
with topic related words trough a backend call.

**Syntax**

```typescript
filterParameters(): void
```

### setParam()

Allows user to click on one of the autocomplete proposals to fill the input
field with the selected one

**Syntax**

```typescript
setParam(param: unknown): void
```

### visible()

For collapsing an insight in order to interact with it.

**Syntax**

```typescript
visible(divId: unknown): void
```

### visible2()

Collapsing _report an error_ interface: After an user has submitted any kind of
error the error interface collapses and the user is
back at the unfolded insight

**Syntax**

```typescript
visible2(divId: unknown): void
```

### visible3()

Submitt-controll: After user selects answer (yellow-status) or confirms an
insight (green-status) further interaction won't be possible anymore.
Function changes displayed div. Button elements with _onclick_ functions beeing
replaced with non-interactable lables

**Syntax**

```typescript
visible3(divId: unknown): void
```

### visible4()

This function assures that there is always only one insight unfolded.
Unfolding another insight automatically collapses the old one

**Syntax**

```typescript
visible4(): void
```

### saveInName()

Saving current insight user has interacted with and commiting it to a state
object in vuex store

**Syntax**

```typescript
saveInName(name: unknown): void
```

### saveAnswerSelection()

Saving selected answer option (yellow-status) and commiting it to a state object
in vuex store

**Syntax**

```typescript
saveAnswerSelection(answer: unknown): void
```

### saveUserInput()

Saving any input user has made and commiting it to a state object in vuex store.
Differentiation between wether it is a new insight answer or a new insight is
handled by calling either _sendUserAnswer_ or _sendUserInsight_ for the given
case.

**Syntax**

```typescript
saveUserInput(): void
```

### sendAnswerSelection()

Triggered right after _saveAnswerSelection(answer)_ to send the selected answer
via api call to the database in the backend.
Afterwards the data gets reloaded to check if an insight has enough upvotes to
change its status to _green status_.
We always store user interaction temporarly into vuex store rather than directly
dispatching it to our backend code.

**Syntax**

```typescript
sendAnswerSelection(): void
```

### sendUserAnswer()

Sending new user _insight answers_ to the database and reloading data to give
the user a direct feedback that his/her new insight is available now.

**Syntax**

```typescript
sendUserAnswer(): void
```

### sendUserInsight()

Sending new user _insight_ to the database and reloading data to give the user a
direct feedback that his/her new insight is available now.

**Syntax**

```typescript
sendUserInsight(): void
```

### sendDownloadRequest()

Triggering direct download

**Syntax**

```typescript
sendDownloadRequest(): void
```

### sendInsightRelevance()

On collapsing any insight this function is triggered to upvote the clicked-on
insight.

**Syntax**

```typescript
sendInsightRelevance(): void
```

### sendInsightNotRelevantError()

Dispatching insight-not-relevant-error to the backend, where it is handled

**Syntax**

```typescript
sendInsightNotRelevantError(): void
```

### sendValueError()

Dispatching value-error to the backend, where it is handled

**Syntax**

```typescript
sendValueError(): void
```

### sendTypoError()

Dispatching typo-error to the backend, where it is handled

**Syntax**

```typescript
sendTypoError(): void
```

### sendScraper()

Triggers backend scraper to scrape further informations for the direct-download
file e.g. Autors, Title etc.
Function is beeing called directly when the component has been _created_ to
guarantee an instant download experience to the users

**Syntax**

```typescript
sendScraper(): void
```

