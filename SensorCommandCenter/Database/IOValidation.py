from cryptography.fernet import Fernet
import os
import re



#This class is designed to validate input and output for unwanted characters or too much length. It raises an error if something is invalid

class InputOutputValidation:

    def validate_user_name(username:str):
        pass

    def validate_user_first_last_name(user_f_name:str, user_l_name:str):
        pass

    def validate_user_pw(pw:str):
        #Check length between min and max (min 12 characters)

        #REGEX Check for unwanted characters and min needed character variety (capital, lower, number, special character)

        pass

    def validate_sensor_name(sensor_name:str):
        #Check length
        if len(sensor_name)>100:
            raise Exception("Sensor name length exceeds 100 character allowance.")

        #Check for invalid characters
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


    