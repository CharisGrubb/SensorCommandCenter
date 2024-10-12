from cryptography.fernet import Fernet
import os



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
        pass

##ENCryptor and DECryptor
class Ryptor:
    __loading_encryption_key = False
    @staticmethod
    def encrypt(data_to_encrypt:str):
        while Ryptor.__loading_encryption_key:
            print('Waiting for encryption key loading to finish...')
        
        key = os.environ.get('SCC_ENC_Key')
        f = Fernet(key)
        token = f.encrypt(data_to_encrypt.encode('utf-8'))

        return token

     

    
    @staticmethod
    def decrypt(data_to_decrypt:str):
        while Ryptor.__loading_encryption_key:
            print('Waiting for encryption key loading to finish...')
        
        key = os.environ.get('SCC_ENC_Key')
        f = Fernet(key)
        token = f.decrypt(data_to_decrypt.encode('utf-8'))

        return token

    
    @staticmethod 
    def load_encryption_key():
        Ryptor.__loading_encryption_key = True
        #Pause to allow any processes in the middle of running to finish pushing through


        old_key = os.environ.get('SCC_ENC_Key','-1')
        key = Fernet.generate_key()
        if old_key != '-1':
            print("Update data with new rotated encryption key.")


        os.environ["SCC_ENC_Key"] = key
        Ryptor.__loading_encryption_key = True



    