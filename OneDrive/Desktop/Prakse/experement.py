import requests
import json
from datetime import datetime
print('start')
# Get the current time.
now=datetime.now()
# Do the request for data.
response = requests.get('https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,,EUR')
# Format now data, to math the data formatting of nordpool.
dateOfInterest = now.strftime('%d-%m-%Y')
# Format request response to JSON.
jayson = json.loads (response.text)
# Loop through relevant data.
for row in jayson ['data']['Rows'] :
    # If is extra row skip, we dont care.
    if row['IsExtraRow']:
        continue
    # Loop through columns array.
    for dayData in row[ 'Columns']:
        # If not today, we don't care.
        if (dayData[ 'Name'] != dateOfInterest):
            continue
        # Split date string to get hours.
        sSplit = row[ 'StartTime'].split('T')
        eSplit = row[ 'EndTime'].split('T')
        # Format output.
        reverse = now.strftime('%Y-%m-%d')
        msg=reverse + ' ' + sSplit [1] + ' - ' + reverse + ' ' + eSplit [1] + ' ' + 'Value: ' + dayData[ 'Value']
        print (msg)