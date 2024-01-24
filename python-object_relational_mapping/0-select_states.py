import MySQLdb
import sys

def get_states(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

 
    # Get command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
 

    # Call the function to get and display states
    get_states(username, password, database)
