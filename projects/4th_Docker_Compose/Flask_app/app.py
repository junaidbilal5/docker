from flask import Flask
import pymysql

app = Flask(__name__)

#
#def get_db_connection():
#    try:
#        connection = mysql.connector.connect(
#            host="mysql_container",
#            #port=3307,
#            user="root",
#            password="rootpassword",
#            database="mydatabase"
#        )
#
#        if connection.is_connected():
#            print("Connected to MySQL Database")
#
#        return connection
#
#    except Error as e:
#        print("Error while connecting to MySQL:", e)
#        return None
#    
@app.route("/")
def home():
    return "Hello, World! flask welcome."

@app.route("/info")
def info():
    return "https://www.linkedin.com/in/junaid-bilal/"




@app.route("/insert_data")

def insert_data():   # function to insert data into MySQL table

    # create connection to MySQL container
    connection = pymysql.connect(
        host="mysql_container",      # Docker container name of MySQL
        user="root",                 # MySQL username
        password="rootpassword",     # MySQL password
        database="mydatabase"        # database name
    )

    cursor = connection.cursor()     # create a cursor object to execute SQL queries

    # SQL query to insert data into users table
    insert_query = "INSERT INTO users(city, temperature) VALUES (%s, %s)"

    data = ('Berlin', 25)   # tuple containing values to insert

    cursor.execute(insert_query, data)   # execute the insert query with provided data

    connection.commit()   # commit the transaction to save changes in database

    cursor.close()   # close the cursor after operation

    connection.close()   # close the database connection

    return "Data inserted successfully"   # return confirmation message   





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)


#http://127.0.0.1:5001/





