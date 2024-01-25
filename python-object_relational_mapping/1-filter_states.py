#!/usr/bin/python3
import MySQLdb
import sys

def filter_states(username, password, database):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query to select states starting with 'N' (case-sensitive)
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;"
        cursor.execute(query)

        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the filter_states function
    filter_states(username, password, database)
