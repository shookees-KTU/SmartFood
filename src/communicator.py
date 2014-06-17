import logging


class Communicator:

    def __init__(self, name):
        self.name = name
        logger = logging.getLogger(__name__ + " " + name)
        logger.info(name + " communicator class initiated")

    def get_name(self):
        pass

    def receive(self):
        pass

    def send(self, contact, content):
        pass

    def get_message(self):
        pass