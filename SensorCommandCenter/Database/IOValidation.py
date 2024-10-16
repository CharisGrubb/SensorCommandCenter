from cryptography.fernet import Fernet
import os
import re



#This class is designed to validate input and output for unwanted characters or too much length. It raises an error if something is invalid
#This is a helper class for the Database Interface. The DB Interface handles checks for usernames/sensornames already existing

class InputOutputValidation:

    @staticmethod
    def validate_user_name(username:str):
        #Check length
        if len(username)>100:
            raise Exception("Username length exceeds 100 character allowance.")

        #Check for invalid characters; whitelist of only lower and upper case alphabet, numbers, and underscore
        check_for_disallowed_characters = re.search("[^A-Za-z0-9_]",username)
        if check_for_disallowed_characters:
            raise Exception("Invalid character [" + check_for_disallowed_characters.group()+ "] detected in Username: {username}")
        

        return username
    
    @staticmethod
    def validate_user_first_last_name(user_f_name:str, user_l_name:str):
        if len(user_f_name)>100 or len(user_l_name)>100:
            raise Exception("User's First or Last name length exceeds 100 character allowance.")

        #Check for invalid characters; whitelist of only lower and upper case alphabet, numbers, and underscore
        check_for_disallowed_characters = re.search("[^A-Za-z0-9'_]",user_f_name)
        if check_for_disallowed_characters:
            raise Exception("Invalid character [" + check_for_disallowed_characters.group()+ "] detected in user's first name")
        
        check_for_disallowed_characters = re.search("[^A-Za-z0-9'_]",user_l_name)
        if check_for_disallowed_characters:
            raise Exception("Invalid character [" + check_for_disallowed_characters.group()+ "] detected in user's last name")
        
        return (user_f_name,user_l_name) #return tuple of name if they pass checks

    @staticmethod
    def validate_user_pw(pw:str):
        #Check length between min and max (min 12 characters)
        if len(pw) < 12:
            raise Exception("Password length requirement not met. Need at least 12 characters.")
        if len(pw)>50:
             raise Exception("Password length too long. Character limit is 50.")

        #REGEX Check for unwanted characters 
        check_for_disallowed_characters = re.search("[^A-Za-z0-9_!@#$%^&*.'`]",pw)
        if check_for_disallowed_characters:
            raise Exception("Invalid character [" + check_for_disallowed_characters.group()+ "] detected in Password.")
        
        #Check for min needed character variety (capital, lower, number, special character)
        if not re.search(r"[a-z]", pw):
            raise Exception("Password requires at least one lower case")
        if not re.search(r"[A-Z]", pw):
            raise Exception("Password requires at least one upper case")
        if not re.search(r"[0-9]", pw):
            raise Exception("Password requires at least one mumber")
        if not re.search(r"[!@#$%&*+=_-]", pw):
            raise Exception("Password requires at least one of the following special characters: !, @, #, $, %, &, *, +, =, _, or -")
        

        #return the password back if it successfully makes it past all checks
        return pw

    def validate_sensor_name(sensor_name:str):
        #Check length
        if len(sensor_name)>100:
            raise Exception("Sensor name length exceeds 100 character allowance.")

        #Check for invalid characters; whitelist of only lower and upper case alphabet, numbers, space, underscore, and hyphen
        check_for_disallowed_characters = re.search("[^A-Za-z0-9 _-]",sensor_name)
        if check_for_disallowed_characters:
            raise Exception("Invalid character [" + check_for_disallowed_characters.group()+ "] detected in Sensor Name: {sensor_name}")
        

        return sensor_name

##ENCryptor and DECryptor
class Ryptor:

    @staticmethod
    def encrypt(data_to_encrypt:str):
      
        
        key = os.environ.get('SCC_ENC_Key')
        f = Fernet(key)
        token = f.encrypt(data_to_encrypt.encode('utf-8'))

        return token

     

    
    @staticmethod
    def decrypt(data_to_decrypt:str):
        
        
        key = os.environ.get('SCC_ENC_Key')
        f = Fernet(key)
        token = f.decrypt(data_to_decrypt.encode('utf-8'))

        return token

    
    @staticmethod 
    def load_encryption_key():
        try:
            key = Fernet.generate_key()
            os.environ["SCC_ENC_Key"] = key

            return True
        except:
            return False


    