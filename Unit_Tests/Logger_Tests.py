from SensorCommandCenter.Logging.Logger import Log


def test_log():
    log = Log('Test','Test')
    log.log_to_database(log_type = 'Test', message='This is a test Log')