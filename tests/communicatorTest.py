from src import communicator
import unittest


class CommunicatorTest(unittest.TestCase):

    def test_get_name(self):
        """
        This test checks for communicator.py name
        """
        name = "CUSTOM COMMUNICATOR NAME"
        c = communicator.Communicator(name)
        self.assertEqual(c.get_name(), name)

    def test_get_message(self):
        """
        This test check for communicator.py receiving a message while sending it to himself
        """
        name = "CUSTOM COMMUNICATOR NAME"
        c = communicator.Communicator(name)
        message = "Test"
        c.send(c.get_name(), message)

    def test_send_receive(self):
        """
        This test creates two communicator.py instances and sends messages one to another
        """
        sender_name = "Sender"
        c_sender = communicator.Communicator(sender_name)

        receiver_name = "Receiver"
        c_receiver = communicator.Communicator(receiver_name)

        message = "Test"
        c_sender.send(c_receiver.get_name(), message)

        self.assertEqual(c_receiver.get_message(), message)
        #switch sides - send echo
        message = "tseT"
        c_receiver.send(c_sender.get_name(), message)
        self.assertEqual(c_sender.get_message(), message)

if __name__ == "__main__":
    unittest.main()