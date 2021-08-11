from datetime import date, datetime
from dateutil.parser import parse


def check(date_to_check) -> bool:
    if isinstance(date_to_check, date) or isinstance(date_to_check, datetime):
        return True

    try:
        parse(date_to_check)
        return True
    except:
        return False
