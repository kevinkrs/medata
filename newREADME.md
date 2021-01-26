# Medata 

Medata is a chrome-plugin that helps researchers to collect and contribute insights/datapoints to a paper listed in the [ACM Digital Library](https://dl.acm.org/).

## Installation Backend

In future the backend is going to be hosted online, to setup your own backend:

* [clone the GitHub repo](https://github.com)
* navigate to the medata_backend folder
* create venv: ```python -m venv venv```
    * ```venv\Scripts\activate.bat```(Windows)
    * ```source venv/bin/activate```(Mac/Linux)
* use [pip](https://pip.pypa.io/en/stable/) to install the requirements: ```pip install -r requirements.txt```
* run app.py to start the backend server


## Installation Frontend

The plugin is available in the [chrome web store](https://chrome.google.com/webstore/category/extensions?hl=en), to setup your own frontend:

* navigate to the medata_frontend folder
* ```npm install```
* ```npm run build```
* open Chrome and search for [chrome://extensions/](chrome://extensions/)
* enable developer mode 
* load unpacked extension 
* select the "dist" folder 




## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Built With

* [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/#) - Backend
  * [sqlite](https://www.sqlite.org/index.html)  - Database
* [vue.js](https://vuejs.org/) - Frontend


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://ct/licenses/mit/)