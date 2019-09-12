"""
This module is for associating contact information--name and number--with user-defined, custom messages.

@author a.k
"""

from app import FROM, wa_client
from app.ContactDirectory import Contacts


class Messenger:
    def __init__(self, cd: Contacts):
        self.contacts: Contacts = cd
        self.draft = {}

    def create_body(self, c_name: str, msg_body: str):
        """
        Maps a contact number to a supplied message body
        :param c_name: contact name
        :param msg_body: body of the message
        :raises Exception if contact name is not in the contact directory
        :return: none
        """
        if c_name in self.contacts.directory:
            self.draft[self.contacts.directory[c_name]] = msg_body
        else:
            raise Exception("Error! contact name not found")

    def send(self):
        """
        Public interface method to send generated message bodies to the contacts specified
        :raises Exception if the draft message dict is empty
        :return: None
        """
        if len(self.draft) <= 0:
            raise Exception("Error! No messages have been created")
        for number, body in self.draft.items():
            Messenger.message(FROM, number, body)

    @staticmethod
    def message(from_: str, to: str, body: str):
        """
        Uses Twilio client to send a message to the given number
        :param from_: message from number
        :param to: message to number
        :param body:  message body
        :return: none
        """
        sent = wa_client.messages.create(
            body=body,
            from_='whatsapp:' + from_,
            to='whatsapp:' + to,
        )
        print(sent.sid)
