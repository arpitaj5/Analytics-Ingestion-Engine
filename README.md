# Analytics-Ingestion-Engine

Team : Asmita, Arpita, Deena, Nishan

**deploy_script.py :** sets up code on ec2 
The query runs on local machine
* First connects to the server
* Clones the code repository from github
* Removes any existing crontab
* Launches server by running `flask_server.py`
**flask_server.py :** takes user input and parses
