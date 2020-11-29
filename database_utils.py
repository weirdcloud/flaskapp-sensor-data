import sqlite3


def create_sql_connection():
    con = sqlite3.connect('sensor_database.db')
    return con


def create_sql_table(con):
    cursor_obj = con.cursor()
    cursor_obj.execute(
        'CREATE TABLE IF NOT EXISTS sensor_data(temperature FLOAT, maximum FLOAT, minimum FLOAT, time TEXT)')
    con.commit()
    cursor_obj.close()


def insert_sql_table(con, temp, maximum, minimum, timestamp):
    cursor_obj = con.cursor()
    cursor_obj.execute(
        '''INSERT INTO sensor_data(temperature, maximum, minimum, time) VALUES(?, ?, ?, ?)''',
        (temp, maximum, minimum, timestamp))
    con.commit()
    cursor_obj.close()


def fetch_last():
    con = create_sql_connection()
    cursor_obj = con.cursor()
    cursor_obj.execute('SELECT * FROM sensor_data ORDER BY time DESC LIMIT 1')
    last = cursor_obj.fetchall()
    cursor_obj.close()
    con.close()
    if len(last):
        last = last[0]
    else:
        last = None
    return last


def fetch_specified(date_limits, temp_limits=(0, 50)):
    con = create_sql_connection()
    cursor_obj = con.cursor()
    cursor_obj.execute('''SELECT * FROM sensor_data WHERE time BETWEEN datetime(?) AND datetime(?) AND temperature BETWEEN ? AND ?''',
                       (date_limits[0], date_limits[1], temp_limits[0], temp_limits[1]))
    records = cursor_obj.fetchall()
    cursor_obj.close()
    con.close()
    return records
