

###Need to add logic to determine file location and ensure cd in the correct spot

python -m venv .venv 
.venv\Scripts\Activate.ps1 #If your powershell execution policy is set to restricted this will not work. 

python -m pip install -r  SensorCommandCenter\requirements.txt  

python "SensorCommandCenter\Install Scripts\Database Files\SQLite (Internal)\database_set_up.py" #Run Internal database install

fastapi dev SensorCommandCenter\main.py #Set for dev currently as testing

