from datetime import datetime


def decode_time(obj, format):
    try:
        parsed_date = datetime.strptime(obj, format)
        return parsed_date.strftime("%Y-%m-%dT%H:%M:%S")
    except:
        return 0
