import logging

class LogGen:
    @staticmethod
    def loggen():
        fhandler = logging.FileHandler(filename='C:\\Projects\\pythonProject\\IdanRealProject\\Logs\\automation.log', mode='a')
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        fhandler.setFormatter(formatter)
        logger = logging.getLogger()

        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger




