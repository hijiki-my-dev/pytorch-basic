import logging


class Logger:
    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        while self.__logger.hasHandlers():
            self.__logger.removeHandler(self.__logger.handlers[0])

        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        self.__logger.addHandler(handler)
        pass

    def debug(self, message: str):
        return self.__logger.dubug(message)

    def info(self, message: str):
        return self.__logger.info(message)

    def warning(self, message: str):
        return self.__logger.warning(message)

    def error(self, message: str):
        return self.__logger.error(message)

    def critical(self, message: str):
        return self.__logger.critical(message)
