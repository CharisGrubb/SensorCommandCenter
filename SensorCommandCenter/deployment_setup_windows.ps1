

###Need to add logic to determine file location and ensure cd in the correct spot

python -m venv .venv 
.venv\Scripts\Activate.ps1 #If your powershell execution policy is set to restricted this will not work. 

python -m pip install -r requirements.txt

python -m &".\Install Scripts\Database Files\SQLite (Internal)\database_setup_py" #Run Internal database install

fastapi dev main.py #Set for dev currently as testing