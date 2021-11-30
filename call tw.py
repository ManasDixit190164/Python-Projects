from twilio.rest import Client

a = 'ACd4337ca12200600509f36bdf420eb583'
at = 'f6b74f6b533ce7613a310d080069dd7e'
client = Client(a,at)
call = client.calls.create(
twiml = '<Response><Say>Hello this is Vinay Mishra</Say></Response>',
to='+917054908887',
from_= '+13187089224'
)
print(call.sid)