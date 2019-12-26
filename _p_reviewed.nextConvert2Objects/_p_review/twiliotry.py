'''
Twilio:
account sid : AC36de5085a7c70b3bcf7a3899fb0b9574
auth token : ab5cdd226bcbdd06595ca91e038ee1b3
twilio number = +19546211371
'''

from twilio.rest import TwilioRestClient
accountSID = AC36de5085a7c70b3bcf7a3899fb0b9574
authToken = ab5cdd226bcbdd06595ca91e038ee1b3

twilioCli = TwilioRestClient(accountSID, authToken)
