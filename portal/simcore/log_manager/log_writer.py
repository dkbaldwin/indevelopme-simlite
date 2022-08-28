import logging
import uuid

##################################################################################
# todo: need to flesh this guy out more
# todo: I would like to integrate this module with splunk so that its job is to
#       supply splunk with the information.
##################################################################################
# serves as an interface to the Logwriter class
def store_log(caller_name, log_message, log_level='warning'):
    temp_logger = LogWriter(caller_name)
    guid = temp_logger.store_app_log(log_message, log_level)
    return guid

class LogWriter:
    logger = None
    formatter = None

    # init logger portal
    def __init__(self, log_object_name='app', filename='app.log'):
        # create logger
        self.logger = logging.getLogger(log_object_name)
        self.logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.FileHandler(filename=filename)
        ch.setLevel(logging.DEBUG)

        # create formatter
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(self.formatter)

        # add ch to logger
        self.logger.addHandler(ch)

    def store_app_log(self, message, level='warning'):
        log_uid = str(uuid.uuid4())
        try:
            if level.lower() == 'warning':
                self.logger.warning(log_uid + '=' + message)

            if level.lower() == 'error':
                self.logger.error(log_uid + '=' + message)

            if level.lower() == 'info':
                self.logger.info(log_uid + '=' + message)

        except Exception as e:
            logging.exception("message")

        return log_uid