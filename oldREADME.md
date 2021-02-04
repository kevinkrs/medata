# WS20 Interactive Labeling

## Python virtual enviroment installieren
1. You have to navigate with the command line to the medata_backend folder
2. Copy this command and press then Enter: python -m venv venv
3. A new Folder called venv is created
4. on Windows copy this: venv\Scripts\activate.bat
5. on Mac or Linux navigate to project folder and run: source venv/bin/activate
6. on the left side of your command line should be a "(venv)" -> then your venv is activated
7. Once your venv is activated enter following command: pip install -r requirements.txt
8. Now your virtual enviroment is ready to rumble!


## Bug Fix download function
In order to get the download function working you have to navigate to the backend folder first and then excecute the the app.py

## Vue Frontend testen
1. chrome:// extension in Chrome öffnen
2. Developer Mode oben rechts aktivieren
3. In medata_plugin Datei "npm run build" ausführen
4. Backend Server starten
5. "dist" Datei in Chrome oben links als "load unpacked" hochladen
6. Plug in oben Rechts in der Pluginzeile aussuchen

## set up a server at Microsoft Azure
1. create a Linux vm with Ubuntu
2. establish a connection to the server - ssh is the easiest
3. "sudo apt update" and "sudo apt upgrade" 
4. follow this instruction: https://docs.microsoft.com/en-us/azure-stack/user/azure-stack-dev-start-howto-vm-python?view=azs-2008
1. change the security network ports
5. instead of starting the server with "flask run -h 0.0.0.0" you should change in app.py in the last line app.run() to app.run(host = "0.0.0.0")
6. Then excecute "pyhton3.8 app.py". The Server runs now in a developement enviroment
7. for a Production enviroment you should set up your server differently
