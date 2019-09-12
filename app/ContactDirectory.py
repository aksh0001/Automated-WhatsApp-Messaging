"""
This module contains information related to WhatsApp contacts.

@author a.k
"""
from app import wa_client


class Contacts:
    def __init__(self):
        self.directory = {}

    def add_contact(self, name: str, ph_no: str):
        """
        Adds a contact into the directory. Takes in name keys and the contact number as the value.
        :param name: name of contact
        :param ph_no: phone number of contact
        :raises Exception if an invalid number is entered
        :return: none
        """
        try:
            ph_no = wa_client.lookups.phone_numbers(ph_no).fetch()
        except Exception:
            raise Exception("Error! invalid number entered")
        self.directory[name] = ph_no.phone_number

    def get_number(self, name: str):
        """
        Returns the number associated with contact name
        :param name: contact name
        :return: the number of the contact
        """
        return self.directory[name]

    def remove_contact(self, name: str):
        """
        Removes a contact from the directory
        :param name: name of contact
        :return: none
        """
        self.directory.pop(name)

    def view_directory(self):
        """
        Displays the directory
        :return: none
        """
        for name, number in self.directory.items():
            print("Name:", name, " | Phone number:", number)
