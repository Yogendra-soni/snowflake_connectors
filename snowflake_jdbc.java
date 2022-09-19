
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;

public class sfk_jdbc
{
  public static void main(String[] args) throws Exception
  {
    Connection connection = getConnection();

    Statement statement = connection.createStatement();

  }
   private static Connection getConnection()
  {
      Class.forName("net.snowflake.client.jdbc.SnowflakeDriver");
   }
    Properties properties = new Properties();
    properties.put("user", "your user name");     
    properties.put("password", "your password"); 
    properties.put("account", "your account name ");  
    properties.put("db", "Databadse name");       
    properties.put("schema", "scheman name");  
    String connectStr = System.getenv("SF_JDBC_CONNECT_STRING");
    
    if(connectStr == null)
    {
     connectStr = "jdbc:snowflake://accountName.snowflakecomputing.com"; // replace accountName with your account name
    }
    return DriverManager.getConnection(connectStr, properties);
  }
}

