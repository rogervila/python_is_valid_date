from dateutil.parser import parse


def check(date) -> bool:
    try:
        parse(date)
        return True
    except:
        return False
