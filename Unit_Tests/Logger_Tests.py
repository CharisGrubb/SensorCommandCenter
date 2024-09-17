from SensorCommandCenter.Logging.Logger import Log


def test_log():
    log = Log('Test','Test')
    log.log_to_database()