import datetime
import myCal


def create_time_slots():
    """Creates the timeslots"""
    start_time = datetime.datetime(1,1,1,8,0,0)
    end_time = datetime.datetime(1,1,1,17,0,0)
    now = datetime.datetime.now()

    time_slots  = []

    while start_time != end_time:
        time_slots.append(start_time)
        start_time = start_time + datetime.timedelta(minutes=30)
    
    return time_slots


def get_booked_time_slots(calendar):
    """Returns the timeslots already booked"""
    booked_slots = []
    for slot in calendar:
        book_timeslot = slot['start_time'].split('+')[0]+'Z'
        booked_slots.append(book_timeslot)
    return booked_slots
        


def get_availble_time_slots(chosen_date):
    """Returns the availble timeslots"""
    time_slots = create_time_slots()
    now = datetime.datetime.now()
    availble_timeslots = [""]
    calendar_data = myCal.get_calendar_data()
    booked_slots = get_booked_time_slots(calendar_data)
    
    for time_slot in time_slots:
        date_time = myCal.return_datetime(chosen_date, time_slot + datetime.timedelta(hours=2))
        time_slot_iso_str = myCal.return_iso_string(date_time)
        if chosen_date == now.date():
            if now.time() < time_slot.time() and time_slot_iso_str not in booked_slots:
                availble_timeslots.append(time_slot)
        else:
            if time_slot_iso_str not in booked_slots:
                availble_timeslots.append(time_slot)
    return availble_timeslots
    
    
def next_seven_days():
    days = [""]
    now = datetime.datetime.now()
    current_day = now
    for i in range(7):
        days.append(current_day.date())
        current_day = current_day + datetime.timedelta(days=1)
        
    return days
        
    
    