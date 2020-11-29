import os
import time
import io
import base64

from flask import Flask, redirect, url_for, request, jsonify, render_template
from plotting_utils import *
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


@app.route('/', methods=['GET', 'POST'])
def show_statistics():
    if request.method == 'POST':
        form_data = request.form
        date_start = form_data['date_start']
        date_end = form_data['date_end']
        data = fetch_specified((date_start, date_end))
        temperature, maximums, minimums, timestamps = parse_graph_data(data)
        plot_url = gen_temp_plot(temperature, maximums, minimums, timestamps)
    else:
        plot_url = None

    last_read = fetch_last()
    return render_template("stats.html", last_read=last_read, plot_url=plot_url)


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
