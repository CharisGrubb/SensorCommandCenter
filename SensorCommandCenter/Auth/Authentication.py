from fastapi import  HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from SensorCommandCenter.Database.Database_Interfaces import InternalDBConnection
from SensorCommandCenter.Logging.Logger import Log
from typing import Annotated


import bcrypt 
import secrets
import traceback



class AuthHandler: 
    security = HTTPBasic()
    def __init__(self):
        self.db = InternalDBConnection()
        self.configs = self.db.get_configurations("Authentication") #Get internal and/or any external configurations configured
        self.log = Log("Authentication","AuthHandler")
     
        

    def authenticate_user(self,credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
        #!!!!Look into lockout after so many failed attempts
        username = credentials.username.encode("utf8")
        password = credentials.password.encode("utf8")
        print('inside for authenticate user', username)
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
            user_authenticated = bcrypt.checkpw(password,user_pw_hash)

       
        ##Else...connect/call integration to others

        self.log.log_to_database("Authentication", username + " authenticated: " + str(user_authenticated)+ " via " + user_account_type, "INFO", None)
        if user_authenticated is True:
            return username
        else:
            raise HTTPException(status_code=401,detail="Incorrect username or password.", headers={"WWWAuthenticate":"Basic"})
    
    def check_user_access(self, access_required = 'ADURC'):
        access_map = 'ADURC'
        user_access_b = '00011' #ADURC 
        user_access_t = "".join(access_level for access_level in access_map if user_access_b[access_map.index(access_level)]==1)
        print(user_access_t)

    #central point for hashing, allowing updates 
    @staticmethod 
    def hash_data(data_to_hash:str):
        try:
            salty = bcrypt.gensalt()
            hashed_data = bcrypt.hashpw(data_to_hash.encode('utf-8'), salt=salty)
            return hashed_data
        except:
            return None
    


