from twilio.rest import Client

TWL_SID = '<YOUR ACCOUNT SID HERE>'
AUTH_TKN = '<YOUR AUTH TOKEN HERE>'

FROM = '<YOUR FROM NUMBER HERE>'

# create client
wa_client = Client(TWL_SID, AUTH_TKN)
