# standard library
from datetime import timedelta, datetime

def iter_time(date, c_timing, i_timing, hours=1):
    """Generator which iterate through time and yields.

    arguments:
    date -- Date which both are available
    c_timing -- candidate timing type: tuple of two datetime.time
    i_timing -- interviewer timing type: tuple of two datetime.time
    hours -- hours of interview default(1)

    yield:
    time1 -- Starting time of available slot
    time2 -- ending time of available slot
    """
    can_time = datetime.combine(date, c_timing[0])
    can_end_time = datetime.combine(date, c_timing[1])

    in_time = datetime.combine(date, i_timing[1])

    while can_time + timedelta(hours=1) <= in_time\
        and can_time + timedelta(hours=1) <= can_end_time:
        
        yield can_time, can_time + timedelta(hours=hours)

        can_time = can_time + timedelta(hours=hours)

def find_time_slots(date, c_timing, i_timing):
    """Return list of tuple contains slots for interviewer and candidates"""
    time_li = list()

    for can_time, int_time in iter_time(date, c_timing, i_timing):
        
        time_li.append(
            (can_time.time().strftime("%I:%M %p"),
            int_time.time().strftime("%I:%M %p"))
        )
    
    return time_li