# Analytics-Ingestion-Engine

Team : Asmita, Arpita, Deena, Nishan

**deploy_script.py :** sets up code on ec2   
The query runs on local machine
* First connects to the server
* Clones the code repository from github
* Removes any existing crontab
* Launches server by running `flask_server.py`  
**flask_server.py :** takes user input and parses
It takes request in the form of **ip:port/<text>**  
* For a valid json blob in <text> the text gets stored in Raw.txt
* The json blob is parsed and stored in proc.txt
