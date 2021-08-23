from datetime import date, timedelta
from datetime import datetime

__today = date.today()
__today_date = str(__today.strftime('%d/%m/%Y'))

__start = (__today + timedelta(days=11))
__minimum_start_date = str(__start.strftime('%d/%m/%Y'))
__flight = __start + timedelta(days=-__start.weekday(), weeks=1)


def flight_start_date():
    flight_monday = str(__flight.strftime('%d/%m/%Y'))
    return flight_monday


def camp_end_date():
    end = __flight + timedelta(days=20)
    end_date = str(end.strftime('%d/%m/%Y'))
    return end_date
