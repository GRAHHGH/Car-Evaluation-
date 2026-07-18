import mysql.connector
import pandas as pd 

try: 
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  
        database="uci_projects"
    )

    cursor = connection.cursor()

    query = "SELECT * FROM car_evaluations;"
    cursor.execute(query)

    raw_data = cursor.fetchall()

    column_header = cursor.column_names

    df = pd.DataFrame(raw_data, columns = column_header)

    print("Data succefully loaded into pandas")
    print(df)

except mysql.connector.ERROR as error:
    print(f"Database error occured {error}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
