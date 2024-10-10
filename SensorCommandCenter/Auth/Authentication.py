from fastapi import Depends, HTTPException, status
from Database.Database_Interfaces import InternalDBConnection


import hashlib 
import secrets
import traceback



class AuthHandler: 

    def __init__(self):
        self.db = InternalDBConnection()
        self.configs = self.db.get_configurations("Authentication") #Get internal and/or any external configurations configured
     
        

    def authenticate_user(username:str, password_hash:str):
        print('Inside get username ')
        current_username_bytes = username.encode("utf8")
        correct_username_bytes = b"JediMaster"
        is_correct_username = secrets.compare_digest(current_username_bytes, correct_username_bytes)

        current_password_bytes = password_hash.encode("utf8")
        correct_password_bytes = b"R2D2_for_President"
        is_correct_password = secrets.compare_digest(current_password_bytes, correct_password_bytes)

        if not(is_correct_username and is_correct_password):
            raise HTTPException(status_code=401,detail="Incorrect username or password.", headers={"WWWAuthenticate":"Basic"})
        
        return username
    

    #central point for hashing, allowing updates 
    @staticmethod 
    def hash_data(data_to_hash:str):
        hashed_objects = {"hash":"","oldHash":"Option for when migrating to new hash algorithm"}

        hashed_objects['hash'] = hashlib.sha384(data_to_hash.encode())
        hashed_objects['oldHash']="N/A-Will be used when updating hash algorithm for future proofing"

        return hashed_objects
    


