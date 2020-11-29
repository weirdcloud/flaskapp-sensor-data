from datetime import datetime


def parse_temp(temp_json):
    temp = temp_json["temperature"]
    max_temp = temp_json["max_temperature"]
    min_temp = temp_json["min_temperature"]
    timestamp = datetime.now()
    return temp, max_temp, min_temp, timestamp
