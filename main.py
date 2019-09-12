"""
Invokes the client
"""
from app.ContactDirectory import Contacts
from app.WhatsAppMessenger import Messenger


def main(event=None, context=None):
    # contact directory - add contacts
    cd = Contacts()
    cd.add_contact('<CONTACT NAME 1>', '<CONTACT NUMBER 1>')
    cd.add_contact('<CONTACT NAME 2>', '<CONTACT NUMBER 2>')
    cd.add_contact('<CONTACT NAME 3>', '<CONTACT NUMBER 3>')
    cd.view_directory()

    msgr = Messenger(cd)
    msgr.create_body('<CONTACT NAME 1>', '<MESSAGE BODY>')  # create messages
    msgr.create_body('<CONTACT NAME 2>', '<MESSAGE BODY')
    msgr.send()  # send created messages to contacts


if __name__ == '__main__':
    print('Testing...')
    main()
