import mysql.connector
  
conn = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "jptv20_moviesdb"
)
 
print(conn)
  
# Disconnecting from the server
conn.close()