# snowflake_connectors

This Repository shows the different connector that can be used to connect snowflake.
It hold the basic connectivity code to connect with snowflake.

##Pythonc snowflake connector:

###Prerequisites:
python 3.6 and above

### Install the Connector:
Instal python connector dependencies:
pip install -r https://raw.githubusercontent.com/snowflakedb/snowflake-connector-python/v2.7.9/tested_requirements/requirements_36.reqs

Install connector
pip install snowflake-connector-python


## JDBC Connector:

###Prerequisites:
Java 1.8 or higher

### Install the driver:
Downloading the Driver from the Maven Central Repository:
https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc

###Integrating the Driver into a Maven Project:
<dependencies>
  ...
  <dependency>
    <groupId>net.snowflake</groupId>
    <artifactId>snowflake-jdbc</artifactId>
    <version>3.13.20</version>
  </dependency>
  ...
</dependencies>


## ODBC driver:

### Install teh driver:
Windows 64 bit: https://sfc-repo.snowflakecomputing.com/odbc/win64/latest/index.html
Windows 32 bit: https://sfc-repo.snowflakecomputing.com/odbc/win32/latest/index.html

### Configure the ODBC Driver:
Launch the Windows Data Source Administration Tool from Windoes start:
![alt text](https://docs.snowflake.com/en/_images/odbc1.png)
Verify that the Snowflake ODBC driver is installed:
![alt text](https://docs.snowflake.com/en/_images/odbc2.png)
Create DSN and provide user Name and passowrd.
