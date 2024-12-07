from fastapi import Depends, HTTPException, status
from SensorCommandCenter.Database.Database_Interfaces import InternalDBConnection
from SensorCommandCenter.Logging.Logger import Log


import bcrypt 
import secrets
import traceback



class AuthHandler: 

    def __init__(self):
        self.db = InternalDBConnection()
        self.configs = self.db.get_configurations("Authentication") #Get internal and/or any external configurations configured
        self.log = Log("Authentication","AuthHandler")
     
        

    def authenticate_user(self,username:str, password:str):
       

        if username is None or password is None:
            raise HTTPException(status_code=401,detail="Incorrect username or password.", headers={"WWWAuthenticate":"Basic"})
        
        ####get user acount type from username
        user_account_type= self.db.get_user_account_type(username)
        user_authenticated=False
       
        ####If user doesn't exist (NONE returned), raise 401 error
        if user_account_type is None:
            raise HTTPException(status_code=401,detail="Incorrect username or password.", headers={"WWWAuthenticate":"Basic"})
       
        ##If internal account...get password hash and check digest
        elif user_account_type == "Internal":
            user_pw_hash = self.db.get_password_hash(username)
            user_authenticated = bcrypt.checkpw(password.encode('utf-8'),user_pw_hash)

       
        ##Else...connect/call integration to others

        self.log.log_to_database("Authentication", username + " authenticated: " + str(user_authenticated)+ " via " + user_account_type, "ERROR", None)
        
        return user_authenticated
    
    

    #central point for hashing, allowing updates 
    @staticmethod 
    def hash_data(data_to_hash:str):
        try:
            salty = bcrypt.gensalt()
            hashed_data = bcrypt.hashpw(data_to_hash.encode('utf-8'), salt=salty)
            return hashed_data
        except:
            return None
    


