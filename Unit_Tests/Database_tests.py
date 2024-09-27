from SensorCommandCenter.Database.Database_Interfaces import InternalDBConnection


def get_all_configs():

    db = InternalDBConnection()
    db.connect()
    results = db.get_configurations('test',"test","test")
    db.close_connection()
    print(results)
    for r in results:
        print(r)
    