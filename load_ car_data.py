import mysql.connector

try: 
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",  
        database="uci_projects"
    )
    cursor = connection.cursor()
    print("successfully added to the database")

    with open("car.data", "r", encoding="utf-8") as file:
        row_count = 0

        for line in file:
            cleaned_line = line.strip()

            if not cleaned_line:
                continue
            
            car_attributes = cleaned_line.split(",")
            insert_query = """
            INSERT INTO car_evaluations (
                buying_price, maint_cost, doors, persons, lug_boot, safety, acceptability_class
            ) VALUES (%s, %s, %s, %s, %s, %s, %s);
            """

            cursor.execute(insert_query, car_attributes)
            row_count += 1
        
    connection.commit()
    print(f"ETL pipeline successful! Successfully inserted {row_count} rows.")
        
except mysql.connector.Error as error:
    print(f"Database error occurred: {error}")

finally:
    # 6. Always clean up and close your connections when done
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed securely.")