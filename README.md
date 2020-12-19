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


## Vue Frontend testen
1. chrome:// extension in Chrome öffnen
2. Developer Mode oben rechts aktivieren
3. In medata_plugin Datei "npm run build" ausführen
4. Backend Server starten
5. "dist" Datei in Chrome oben links als "load unpacked" hochladen
6. Plug in oben Rechts in der Pluginzeile aussuchen