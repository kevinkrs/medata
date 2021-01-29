# About

Main logic of the plugin opening page.

## Data

| Name          | Type     | Description                                                                  | Initial value                                                            |
| ------------- | -------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `substr`      | `regexp` | Checking if user is on any dl.acm.org page                                   | `/dl\.acm\.org\//`                                                       |
| `regex`       | `regexp` | Checking for specific paper. Available in pdf and epdf view as well.         | `/dl\.acm\.org\/doi\/((fullHtml\/)|(epdf\/)|(pdf\/)){0,1}\d+\.\d{3,}\//` |
| `regexBinder` | `regexp` | Checking for specific Binder page                                            | `/dl\.acm\.org\/action\/showBinder\?/`                                   |
| `readingList` | `regexp` | Checking for Binder overview page                                            | `/dl\.acm\.org\/action\/showMyBinders/`                                  |
| `status`      | `number` | Purpose is to load the right vue component depending on the current user url | `0`                                                                      |

## Methods

### checkURL()

This function checks the current tab URL using the regular expressions from
_data_. To get the current tab url we use _backgroundscript.js_ which is capable
of communication between
the extension and the browser application.
If it is on _dl.acm.org_ the system is going to save the URl inside a state
object in vuex store.
Afterwards the _loadData()_ function is beeing triggerd.
If the user is inside his/ her Binder, the Binder.vue component is beeing
loaded.

**Syntax**

```typescript
checkURL(): void
```

### loadData()

This function is called by _checkURL()_. If the user is on a valid page the
function
responsible for fetching backend data is going do be dispatched and only if
resolved the route is going to push the user to our main page
with all the data already available

**Syntax**

```typescript
async loadData(): Promise
```

