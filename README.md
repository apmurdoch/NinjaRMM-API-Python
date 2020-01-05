# NinjaRMM API-Python
This is a simple wrapper to authenticate against the NinjaRMM API with Python.
## Required Python modules
- requests
- datetime
- base64
- hashlib
- hmac
## Usage
An example to get all customers is included.
The API documentation can be found [here](https://www.ninjarmm.com/dev-api).
Remember that the API limits are quite severe - apparently List API requests are expensive and they have limited these to 10 in every 10 minute period. Entity queries are a bit better, with 10 allowed per minute.
## Feature Requests/Alternatives
I just knocked this up as an authentication wrapper, but may add more functionality depending on what we end up doing with the API. For alternatives:

More advanced features are available with Guy Zuercher's [py-ninjarmm-api-client](https://pypi.org/project/py-ninjarmm-api-client/)

Max Anderson also has an excellent PowerShell module available [here](https://github.com/MaxAnderson95/PoSH-NinjaRMM)