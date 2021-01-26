# Medata 

Medata is a chrome-plugin that helps researchers to collect and contribute insights to a paper listed in the [ACM Digital Library](https://dl.acm.org/).

## Installation Backend

In future the backend is going to be hosted online, to setup your own backend:

* clone the GitHub repo ```TODO: link to out repo```
* navigate to the medata_backend folder
* create venv: ```python -m venv venv```
    * run ```venv\Scripts\activate.bat``` (Windows)
    * or ```source venv/bin/activate``` (Mac/Linux) to activate the virtual environment 
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
* select the newly created dist-folder 


# Documentation
Detailed documentation:

* [Backend](medata_backend/documentation_backend.md)
  * [__](medata_backend/docs/__init__.html)[init__.py](medata_backend/docs/__init__.html)
  * [acm_scraper.py](medata_backend/docs/acm_scraper.html)
  * [api.py](medata_backend/docs/api.html)
  * [app.py](medata_backend/docs/app.html)
  * [create_real_data.py](medata_backend/docs/create_real_data.html)
  * [models.py](medata_backend/docs/models.html)
* [Frontend](medata_plugin/documentation_frontend.md)


## Usage
Go on a [ACM Digital Library](https://dl.acm.org/) website, and click on the plugin to load the available data for the selected paper.
![main](medata_backend/example_pictures/main.png)

Green insights hold confirmed answers, while answers in a yellow insight still need to be validated by other users. Red insights are without answers - so feel free to add one!

Insights themselves are listed depending on the categories of the paper. But you can always add one and thereby contribute to our database!

The implemented download function allows you to download either the confirmed insights for the selected paper or 
the confirmed insights for multiple papers stored in an ACM-Binder.  

![download_binder](medata_backend/example_pictures/download_binder.png)

Our plugin relys on a supportive community so please add answers and new insights, confirm existing answers and make use of the report an error function to improve the quality of our database!

## Built With

* [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/#) - Backend
  * [sqlite](https://www.sqlite.org/index.html)  - Database
* [vue.js](https://vuejs.org/) - Frontend


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors and acknowledgment
The plugin and the underlying logic was developed by
Kevin Kraus, Max Heydemann, Jan Effenberger, Jan Bode with the support of Merlin Knäble and Tim Rietz 

@IISM - Karlsruhe Institute of Technology

## License
[MIT](LICENSE.md)