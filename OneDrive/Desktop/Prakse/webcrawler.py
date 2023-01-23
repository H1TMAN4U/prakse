import requests
import json
from datetime import datetime

now=datetime.now()

# response = requests.get('https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,,EUR')
# print(response)

dateOfInterest = now.strftime('%d-%m-%Y')
print(dateOfInterest)

# jayson = json.loads (response.text)
# print(jayson)