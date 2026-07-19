import mysql.connector
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

try: 
    connection = mysql.connector.connect(
        host="db",
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

except mysql.connector.Error as error:
    print(f"Database error occured {error}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()

for col in df.columns:
    df[col] = df[col].astype(str).str.strip()

price_map = {'vhigh': 4, 'high': 3, 'med': 2, 'low': 1}
df['buying'] = df['buying'].map(price_map)
df['maint'] = df['maint'].map(price_map)

doors_map = {'2': 2, '3': 3, '4': 4, '5more': 5}
df['doors'] = df['doors'].map(doors_map)

persons_map = {'2': 2, '4': 4, 'more': 5}
df['persons'] = df['persons'].map(persons_map)

lug_boot_map = {'small': 1, 'med': 2, 'big': 3}
df['lug_boot'] = df['lug_boot'].map(lug_boot_map)

safety_map = {'low': 1, 'med': 2, 'high': 3}
df['safety'] = df['safety'].map(safety_map)

class_map = {'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}
df['class_value'] = df['class_value'].map(class_map)

df = df.dropna()

print("Success transform, Remaining rows:", len(df))
print(df.head())

X = df.drop('class_value', axis=1)
y = df['class_value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

score = accuracy_score(y_test, predictions)
print(f"ML model score {score * 100:.2f}% accuracy")   