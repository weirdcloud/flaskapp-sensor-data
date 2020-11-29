import os
import time

from flask import Flask, request, jsonify, render_template
from database_utils import *
from parsing_utils import *

# adjusting timezone
os.environ["TZ"] = "Europe/Kiev"
time.tzset()

# initialising database
con = create_sql_connection()
create_sql_table(con)
con.close()

# creating app object
app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_statistics():
    last_read = fetch_last()
    return render_template("stats.html", last_read=last_read)


@app.route('/sensor', methods=['POST'])
def receive_sensor_data():
    temp = request.get_json()
    print(temp)

    # parsing json
    temp, max_temp, min_temp, timestamp = parse_temp(temp)
    print(temp, max_temp, min_temp, timestamp)

    # writing to database
    connection = create_sql_connection()
    insert_sql_table(connection, temp, max_temp, min_temp, timestamp)
    connection.close()

    # return a response
    res = {'status': 'ok'}
    return jsonify(res)
