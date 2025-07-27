MINUTES = 60
HOURS_IN_DAY = 24
DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']


def add_time(start: str, duration: str, _day: str = '') -> str:
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if period.upper() == 'PM' and start_hour != 12:
        start_hour += 12
    elif period.upper() == 'AM' and start_hour == 12:
        start_hour = 0

    dur_hour, dur_minute = map(int, duration.split(':'))

    end_minute = start_minute + dur_minute
    extra_hour = end_minute // MINUTES
    end_minute = end_minute % MINUTES

    end_hour = start_hour + dur_hour + extra_hour
    days_later = end_hour // HOURS_IN_DAY
    end_hour = end_hour % HOURS_IN_DAY

    if end_hour == 0:
        display_hour = 12
        display_period = 'AM'
    elif end_hour < 12:
        display_hour = end_hour
        display_period = 'AM'
    elif end_hour == 12:
        display_hour = 12
        display_period = 'PM'
    else:
        display_hour = end_hour - 12
        display_period = 'PM'

    day_part = ''
    if _day:
        day_index = DAYS_OF_WEEK.index(_day.strip().capitalize())
        new_day_index = (day_index + days_later) % 7
        day_part = f", {DAYS_OF_WEEK[new_day_index]}"

    if days_later == 1:
        later_text = " (next day)"
    elif days_later > 1:
        later_text = f" ({days_later} days later)"
    else:
        later_text = ""

    # Final string
    new_time = f"{display_hour}:{end_minute:02d} {display_period}{day_part}{later_text}"
    return new_time


# Pruebas
if __name__ == '__main__':
    print(add_time('3:00 PM', '3:10'))  # 6:10 PM
    print(add_time('11:30 AM', '2:32', 'Monday'))  # 2:02 PM, Monday
    print(add_time('11:43 AM', '00:20'))  # 12:03 PM
    print(add_time('10:10 PM', '3:30'))  # 1:40 AM (next day)
    # 12:03 AM, Thursday (2 days later)
    print(add_time('11:43 PM', '24:20', 'tueSday'))
    print(add_time('6:30 PM', '205:12'))  # 7:42 AM (9 days later)
