import pyodbc
import sys,os,time


conn = pyodbc.connect("Driver={SnowflakeDSIIDriver}: Server='server address of your snowflake account'; UID = 'User ID"; PWD = 'Password")
                      
cus=conn.cursor()
                      
cus.execute(" copt into test_table from "@snowflake_Stage_name/file_name")
