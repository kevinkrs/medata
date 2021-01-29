# Binder

## Data

| Name            | Type      | Description | Initial value |
| --------------- | --------- | ----------- | ------------- |
| `legendVisible` | `boolean` |             | `false`       |

## Methods

### openGit()

chrome extension call to _background.js_ for opening a new

**Syntax**

```typescript
openGit(): void
```

### setBinder()

To get all available data the backend needs all the paper urls from the binder.
In order to get this information
the _content-script.js_ of the chrome extension is triggered with _setBinder()_.
There a counterpart awaiting the call to provide the requested DOM elements.
After sending the request the function awaits a response which is handled with
the function bellow.

**Syntax**

```typescript
setBinder(): void
```

### sendBinder()

The repsonse from the _content-script.js_ is handled inside here and first
commited to a state object inside vuex store and aftewards
dispatcht to the backend where the available data is bundled and sent back as
direct download.

**Syntax**

```typescript
sendBinder(responseDom: unknown): void
```

