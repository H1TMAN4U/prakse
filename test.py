from worker import *
from main import *
config = ConfigParser()
config.read('config.ini')
mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')
connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
logger = logging.getLogger('root')

prices=select_prices()
consumption=select_consumption()

fixed_cost=float(config.get('fixed_price','fixed_LV_price'))
print(fixed_cost)

# automaticsaving(prices,consumption)


nord_price=[]
fixed_price=[]
usage_array=[]

mycursor = connection.cursor()
mycursor.execute("SELECT price FROM prices;")
prices_table = mycursor.fetchall()
for price in prices_table: 
    nord_price.append(price[0])
print(nord_price)

# print(nord_price*fixed_cost)

# print(saved_EUR)