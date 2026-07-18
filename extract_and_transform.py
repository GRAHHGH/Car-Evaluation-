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
    print(df.head())

    price_map = {"low":1, "med":2, "high":3, "vhigh":4}
    door_map = {"1":1, "2":2, "3":3, "4":4, "5more":5}
    persons_map = {"1":1, "2":2, "3":3, "4":4, "more":5}
    boot_map = {"small":1, "med":2, "big":3}
    safety_map = {"low":1, "med":2, "high":3}
    class_map = {'unacc':0, 'acc':1, 'good':2, 'vgood':3}

    df['buying_price'] = df["buying_price"].map(price_map)
    df['maint_cost'] = df["maint_cost"].map(price_map)
    df['doors'] = df['doors'].map(door_map)
    df['persons'] = df['persons'].map(persons_map)
    df['lug_boot'] = df['lug_boot'].map(boot_map)
    df['safety'] = df['safety'].map(safety_map)
    df['acceptability_class'] = df["acceptability_class"].map(class_map)

    print("Success transform")
    print(df.head())

except mysql.connector.ERROR as error:
    print(f"Database error occured {error}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
