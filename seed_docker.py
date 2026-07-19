import mysql.connector
import csv

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        database="uci_projects",
        port=3307 
    )
    cursor = connection.cursor()
    print("Successfully connected to Docker! Building table...")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS car_evaluations (
        buying VARCHAR(50),
        maint VARCHAR(50),
        doors VARCHAR(50),
        persons VARCHAR(50),
        lug_boot VARCHAR(50),
        safety VARCHAR(50),
        class_value VARCHAR(50)
    )
    """)

    print("Reading car.data and inserting rows...")
    with open('car.data', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row: 
                cursor.execute("INSERT INTO car_evaluations VALUES (%s, %s, %s, %s, %s, %s, %s)", row)

    connection.commit()
    print("All data is securely locked inside Docker")

except mysql.connector.Error as error:
    print(f"Database error occurred: {error}")
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()