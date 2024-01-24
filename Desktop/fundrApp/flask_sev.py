from flask import Flask, jsonify
import pymysql
import pymysql.cursors
import traceback
import logging
import traceback

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


# Type annotations can clarify what the function returns, in this case, a pymysql connection object.
def get_database_connection() -> pymysql.connections.Connection:
    # Use the details from your cloud database service.
    return pymysql.connect(
        host="sql6.freesqldatabase.com",  # Replace with the host from the email.
        user="sql6679269",  # Replace with the username from the email.
        password="NyUU72zQHz",  # Replace with the password from the email.
        db="sql6679269",  # Replace with the database name from the email.
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/get_data', methods=['GET'])
def get_data():
    # No changes required here unless the table name changes.
    connection = get_database_connection()
    try:
        logging.info("Connected to the database successfully.")
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM fundr_alx")
            result = cursor.fetchall()
            return jsonify(result)
    except Exception as e:
        logging.error(f"Error: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()
        logging.info("Database connection closed.")



@app.route('/get_family_data/<int:family_id>', methods=['GET'])
def get_family_data(family_id):
    connection = get_database_connection()
    try:
        logging.info("Connected to the database successfully.")
        with connection.cursor() as cursor:
            # Query to select a specific family by ID
            query = "SELECT * FROM fundr_alx WHERE ID = %s"
            cursor.execute(query, (family_id,))
            result = cursor.fetchone()  # Fetches only one record
            if result:
                return jsonify(result)
            else:
                return jsonify({"error": "Family not found"}), 404
    except Exception as e:
        logging.error(f"Error: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()
        logging.info("Database connection closed.")



if __name__ == '__main__':
    app.run(debug=True)
