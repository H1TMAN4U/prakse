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
# fixed_price=[]
fixed_usage=[]
nord_usage=[]
cheapest_usage=[]
temp_array=[]
main_array=[]
fixed_cost=float(config.get('fixed_price','fixed_LV_price'))
mycursor = connection.cursor()
mycursor.execute("SELECT * FROM electricity_used;")
electricity_used = mycursor.fetchall()

for i in range(0,len(electricity_used)):
    res=(electricity_used[i][0],electricity_used[i][1],float(electricity_used[i][2])*float(fixed_cost))
    fixed_usage.append(res)
# print('fixed_usage',fixed_usage[0])

mycursor.execute("SELECT * FROM prices;")
prices = mycursor.fetchall()

for i in range(0,len(electricity_used)):
    res=(prices[i][0],prices[i][1],1,float(prices[i][3])*float(electricity_used[i][2]))
    nord_usage.append(res)
# print('nord_usage', nord_usage[0])

for i in range(0,len(nord_usage)):
    if nord_usage[i][0] == fixed_usage[i][0]:
        if  nord_usage[i][3] < fixed_usage[i][2]:
            dif=fixed_usage[i][2] - nord_usage[i][3]
            cheapest_usage.append(dif)
            # print(cheapest_usage[0])
            print([res[0],res[1], nord_usage[i][2], cheapest_usage[i]])
            # print('cheapest_usage',cheapest_usage[i])
        else:
            cheapest_usage.append(fixed_usage[i])

# print(cheapest_usage)
#     # except mysql.connector.Error as e:
#     #     logger.error("Error using select_consumption", e)
