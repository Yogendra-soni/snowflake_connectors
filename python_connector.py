# first install pip install --upgrade snowflake-connector-python

import snowflake.connector

# provide details

USER = 'Your_user_name'
PASSWORD = 'yourpassword'
account='Name of your account"
warehouse='Warehpuse Name"
Database= 'Database Name"
Schema='Your schema name"

#create Connections

conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA
    )
    
#create cursor
curs=conn.cursor()

#execute ANy SQL statement
curs.execute(“select current date;”)

#fetch result
print cur.fetchone()[0]


#Loading any file to snowflake copy into via snowflake connector 
cur.execute("copy into table_name from (select * from '@sfk_stage_name/File_path/filename.csv') pattern= '.*.csv' file_format = (type='csv') ")
