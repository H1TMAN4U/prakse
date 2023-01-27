from main import *
import numpy as np
config = ConfigParser()
config.read('config.ini')
mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')
connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
logger = logging.getLogger('root')

# def saved_EUR(start_time,end_time):
#     try:
nord_price=[]
# fixed_price=[]
usage_array=[]
temp=[]

fixed_cost=float(config.get('fixed_price','fixed_LV_price'))
mycursor1 = connection.cursor()
mycursor1.execute("SELECT * FROM electricity_used;")
electricity_used = mycursor1.fetchall()

for i in range(0,len(electricity_used)):
    res=(electricity_used[i][0],electricity_used[i][1],float(electricity_used[i][2])*float(fixed_cost))
    usage_array.append(res)
mycursor1.execute("SELECT * FROM prices;")
prices = mycursor1.fetchall()

for i in range(0,len(electricity_used)):
    res=(prices[i][0],prices[i][1],1,float(prices[i][3])*electricity_used[i][2])
    nord_price.append(res)
array3=[]

for i in range(0,len(nord_price)):
    if nord_price[i][0]==usage_array[i][0]:
        if nord_price[i][3]<usage_array[i][2]:
            dif=usage_array[i][2]-nord_price[i][3]
            print(dif)
            for 
            array3.append(nord_price[i])
            # insert statement for 
        else:
            array3.append(usage_array[i])
# print(array3)
    # except mysql.connector.Error as e:
    #     logger.error("Error using select_consumption", e)
