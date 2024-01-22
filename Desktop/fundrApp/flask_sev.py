from flask import Flask, jsonify
import pymysql
import traceback

app = Flask(__name__)


def get_database_connection():
    # Update with your database credentials
    return pymysql.connect(
        host="localhost",
        user="root",
        password="@n@ALX2024",
        db="alx_dola",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/get_data', methods=['GET'])
def get_data():
    connection = get_database_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM fundr_alx")
            result = cursor.fetchall()
            return jsonify(result)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()


@app.route('/get_family_data/<int:family_id>', methods=['GET'])
def get_family_data(family_id):
    connection = get_database_connection()
    try:
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
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()


if __name__ == '__main__':
    app.run(debug=True)
