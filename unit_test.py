from SensorCommandCenter.Auth.Authentication import AuthHandler
from SensorCommandCenter.Database.IOValidation import InputOutputValidation as IOV
from SensorCommandCenter.Database import Database_Interfaces
import unittest 
import datetime


class Authorization_Tests(unittest.TestCase):

    def test_valid_username(self):
        
        self.assertEqual('admin', IOV.validate_user_name('admin'))
        
    def test_invalid_username(self):
        # from SensorCommandCenter.Database.IOValidation import InputOutputValidation
        self.assertRaises(Exception, IOV.validate_user_name, "' OR 1=1--")

    def test_access_conversions(self):
        print(AuthHandler.convert_access_to_int('CRUDA'))
        # self.assertEqual(1,AuthHandler.convert_access_to_int('C'))
        self.assertEqual('C',AuthHandler.convert_int_to_access(1))

       

class DB_Tests(unittest.TestCase):
    db = Database_Interfaces.InternalDBConnection()

    def test_input_injection(self):
        pass

    def test_add_sensor(self):
        self.assertEqual(1, self.db.add_sensor('TEST SENSOR', 'Unit Test', 'Temperature', 'Manual', None))

    def test_get_sensors(self):
        self.assertIs(type(self.db.get_all_sensors()), list) #Ensure executes without failure and returns list object

    def test_insert_data_point(self):
        
        sensors = self.db.get_all_sensors()
        if len(sensors):
            self.assertEqual(1, self.db.add_sensor_datapoint(sensors[0]['sensor_id'],33.3,datetime.datetime.now()) )
        else: 
            raise Exception("No sensors added in order to test data point insert.")
        
    def test_getting_password_hash(self):
        print("GO GET USERS")
        users = self.db.get_all_users()
        print('USERS',users)
        if users is None or not len(users):
            raise Exception("No users for testing password hash")
        for user in users:
            with self.subTest(user=user):
                self.assertIsNotNone(self.db.get_password_hash(user['username']), f"No PW for user {user['username']}")


if __name__ == '__main__':
    unittest.main()