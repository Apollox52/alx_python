#!/usr/bin/python3
import MySQLdb
import sys

def filter_cities(username, password, database, state_name):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query to select cities of the given state
        query = """
            SELECT cities.name
            FROM cities
            LEFT JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id;
        """
        cursor.execute(query, (state_name,))

        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()

        # Display the results
        if results:
            city_names = ', '.join(result[0] for result in results)
            print(city_names)
        else:
            if cursor.rowcount == 0:
                print("The specified state does not exist.")
            else:
                print("No cities found for the given state.")

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv)
