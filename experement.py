import requests
import json
from datetime import datetime
from main import *
from worker import *
print('start')
now=datetime.now()
response = requests.get('https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,,EUR')
dateOfInterest = now.strftime('%d-%m-%Y')
jayson = json.loads (response.text)
config = ConfigParser()
config.read('config.ini')
mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')
connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)

logger = logging.getLogger('root')

# Inserts data into prices table
def insert_nordpool_prices(start_time,end_time,price):
    try:
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO prices (`start_time`,`end_time`,`price`,`electricity_id`) 
	    VALUES (%s, %s, %s,%s) """       
        record = (start_time,end_time,price,1)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        logger.info(" inserted successfully in price")    

    except mysql.connector.Error as error:
        logger.error("Failed to insert into MySQL table {}".format(error))

for row in jayson ['data']['Rows'] :
    if row['IsExtraRow']:
        continue
    for dayData in row[ 'Columns']:
        if (dayData[ 'Name'] != dateOfInterest):
            continue
        sSplit = row[ 'StartTime'].replace('T', ' ')  
        eSplit = row[ 'EndTime'].replace('T', ' ')    
        msg=sSplit+ ' ' + '-' + ' ' + eSplit+ ' ' + 'Value: ' + dayData[ 'Value']
        print (msg)
        startime=datetime.strptime(sSplit,"%Y-%m-%d %H:%M:%S")
        endtime=datetime.strptime(eSplit,"%Y-%m-%d %H:%M:%S")
        sSplit=startime
        eSplit=endtime
        value=dayData['Value'].replace(",",".")
        value=float(value)
        converted_val=value/1000
        insert_nordpool_prices(sSplit,eSplit,converted_val)
        create_consumtion(sSplit,eSplit)