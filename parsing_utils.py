from datetime import datetime
from matplotlib.dates import date2num


def parse_temp(temp_json):
    temp = temp_json["temperature"]
    max_temp = temp_json["max_temperature"]
    min_temp = temp_json["min_temperature"]
    timestamp = datetime.now()
    return temp, max_temp, min_temp, timestamp


def parse_graph_data(data):
    temperature = []
    maximums = []
    minimums = []
    timestamps = []

    for row in data:
        temperature.append(row[0])
        maximums.append(row[1])
        minimums.append(row[2])
        timestamps.append(row[3])

    timestamps = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S.%f') for t in timestamps]
    timestamps = [date2num(t) for t in timestamps]
    return temperature, maximums, minimums, timestamps
