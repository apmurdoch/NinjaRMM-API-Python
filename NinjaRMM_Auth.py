import requests
from datetime import datetime
import base64
from hashlib import sha1
import hmac

Encoding = 'utf-8'
NinjaAPIURL = 'https://api.ninjarmm.com'                    # Base URL (note some EU users may be https://eu-api.ninjarmm.com)
NinjaAccessKey = 'KeyIDhere'                                # Your Access Key
NinjaSecret = 'SecretHere'                                  # Your Secret
Request = '/v1/customers'                                   # Request URI

# Get the time
Time = datetime.utcnow()
Time = Time.strftime('%a, %d %b %Y %H:%M:%S %z') + 'GMT'

# Construct the string for the signature
String = 'GET\n\n\n' + Time + '\n' + Request
String64 = base64.b64encode(String.encode(Encoding))
# Create the signature
Signature = hmac.new(NinjaSecret.encode(Encoding), String64, sha1)
Signature = base64.b64encode(Signature.digest())
# Create the authorisation string
auth = 'NJ ' + NinjaAccessKey + ':' + Signature.decode(Encoding)

# Example Request - this would get all customers. Remember the severe rate limits Ninja impose
customers = requests.get(NinjaAPIURL+Request, headers={
    'Authorization': auth, 'Date': Time
})
print(customers.content)