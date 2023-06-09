from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from create_token import create_token
from datetime import datetime, timedelta
from event import *
import json
import os
from code_clinic.code_clinic_helper import set_calendar_access_rule, refreshToken
from output_functions import *
from timeslot_functions import get_availble_time_slots, next_seven_days
from prettytable import PrettyTable


def return_email(username):
    """Returns the user email"""
    return f'{username}@student.wethinkcode.co.za'


def get_action(user_type):
    """Gets and Returns the action to take from the user"""
    
    action = ''
    valid_actions = ["view calendar", "book session", " volunteer session",
                     "cancel booking", "cancel volunteering", "1", "2", "3", "4", "5", "help", "q"]
    print(f"{get_output_prefx(user_type)}Select An Option From Below...\n\n \t\t1. view calendar\n \t\t2. book session\n \t\t3. volunteer session\n \t\t4. cancel booking\n \t\t5. cancel volunteer session\n")
    while action not in valid_actions:
        action = input(
            f'{get_output_prefx(user_type)}Enter valid action: ').lower()
    return action


def get_calendar_id():
    """Returns the codeclinic calendar id"""
    return 'jhb19.wethinkcode@gmail.com'


def get_next_seven_days(service, calendar_id=get_calendar_id()):
    """Gets and returns the next seven days from the calendar"""
    
    now = f'{datetime.utcnow().isoformat()}Z'
    events_result = service.events().list(calendarId=calendar_id, timeMin=now,
                    maxResults=200, singleEvents=True, orderBy='startTime').execute()
    events_list = events_result.get('items', [])
    today = datetime.now()
    seven_day_later = today + timedelta(days=6)
    next_seven_day_events = []
    for event in events_list:
        year, month, day = event['start']['dateTime'].split(
            'T')[0].split('-')  # list with [year, month, day]
        start_datetime = datetime(int(year), int(month), int(day), 0, 0, 0)

        if (
            start_datetime <= seven_day_later
            and event['location'] == 'WeThinkCode Joburg Campus'
        ):
            next_seven_day_events.append(event)

    return next_seven_day_events


def structure_data(data):
    """Stuctures the data correctly. Rerutns a list of seven days"""
    
    seven_days = []
    for event in data:
        event_info = structure_event_info(event)
        seven_days.append(event_info)
        
    return seven_days


def structure_event_info(event):
    """Structures event information"""
    
    event_desc = event['description'] if 'description' in event.keys(
    ) else 'Tutoring Session'
    return {
        "id": event['id'],
        "summary": event['summary'],
        "description": event_desc,
        "htmlLink": event['htmlLink'],
        "volunteer": event['creator'].get('email'),
        "attendees": event['attendees'],
        "start_time": event['start'].get('dateTime', event['start'].get('date')),
        "end_time": event['end'].get('dateTime', event['start'].get('date'))
    }


def store_next_seven_days(service):
    """Get amd stores the next seven days"""
    
    latest = False 
    if os.path.exists('calendar.json'):  
        if not latest:
            with open('calendar.json', 'w') as f:
                data = get_next_seven_days(service)
                seven_days = structure_data(data)
                json.dump(seven_days, f, indent=2)
    else:
        with open('calendar.json', 'w') as f:
            data = get_next_seven_days(service)
            seven_days = structure_data(data)
            json.dump(seven_days, f, indent=2)


def store_personal_calendar(service):
    """Stores the users personal codeclinic calendar info in a json file"""
    
    latest = False
    if os.path.exists('student_calendar.json'):  
        if not latest:
            with open('student_calendar.json', 'w') as f:
                data = get_next_seven_days(service, calendar_id='primary')
                seven_days = structure_data(data)
                json.dump(seven_days, f, indent=2)
    else:
        with open('student_calendar.json', 'w') as f:
            data = get_next_seven_days(service, calendar_id='primary')
            seven_days = structure_data(data)
            json.dump(seven_days, f, indent=2)


def get_calendar_data(student=False):
    """Gets and Returns calendar data from json file"""
    
    if not student:
        with open('calendar.json') as f:
            calendar_data = json.loads(f.read())
    else:
        with open('student_calendar.json') as f:
            calendar_data = json.loads(f.read())

    return calendar_data


def get_student_username(event):
    """Gets the username from an event object"""
    
    volunteer = event['volunteer'].split('@')[0]
    if len(event['attendees']) != 3:
        student = "-"
    else:
        for attendee in event['attendees']:
            attendee_username = attendee['email'].split('@')[0]
            if attendee_username not in [volunteer, 'jhb19.wethinkcode']:
                student = attendee_username
    return student


def display_calendar_table(events, student=False):
    """Displays the calendar on the terminal in a table"""
    
    output_str = (
        bold_green("\nYour personal codeclinic calendar:")
        if student
        else bold_blue("\nJHB19 codeclinic calendar:")
    )

    mytable = (
        PrettyTable(["Volunteer", "student", "Date", "Time", "Description"])
        if student
        else PrettyTable(["Availability", "Volunteer", "student", "Date", "Time"]))

    for event in events:
        date, time = event['start_time'].split('T')
        start_time = time.split('+')[0]
        end_time = event['end_time'].split('T')[1].split('+')[0]
        avalibility = event['summary']
        desc = event['description']
        volunteer = event['volunteer'].split('@')[0]
        student_username = get_student_username(event)

        if not student:
            mytable.add_row(
                [avalibility, volunteer, student_username, date, f"{start_time} - {end_time}"])
        else:
            mytable.add_row([volunteer, student_username, date,
                            f"{start_time} - {end_time}", desc])

    print(output_str)
    print(mytable)


def view_calendar(service):
    """Handles the view calendar functionality"""
    
    events = get_calendar_data()
    student_events = get_calendar_data(student=True)

    if not events:
        print('No slots found.')
        return

    display_calendar_table(student_events, student=True)
    display_calendar_table(events)


def display_event_data(event, flag=False, flag2=False):
    """Displays the event data"""
    
    date, time = event['start_time'].split('T')
    start_time = time.split('+')[0]
    end_time = event['end_time'].split('T')[1].split('+')[0]
    if not flag:
        print(f"\n{event['summary']}\nVolunteer: {event['volunteer'].split('@')[0]}\nDate: {date}\
\nTime: {start_time} - {end_time}\n")
    elif flag:
        print(f"{event['summary']}\n\tVolunteer: {event['volunteer'].split('@')[0]}\n\tDate: {date}\
\n\tTime: {start_time} - {end_time}\n")
    elif flag2:
        print(f"\t{event['summary']}\n\tVolunteer: {event['volunteer'].split('@')[0]}\n\tDate: {date}\
\n\tTime: {start_time} - {end_time}\n")


def get_description(username):
    """Gets and Returns the description from the user"""
    
    desc = ''
    while not desc or desc.isdigit():
        desc = input(
            f"{get_output_prefx(username)}What do you need help with? ")
    return desc


def update_calendar(calendar, event_id, updated_event=None):
    """Updates codeclinic calendar and calendar.json files"""
    
    for index, event in enumerate(calendar):
        if event['id'] == event_id and updated_event:
            calendar[index] = structure_event_info(updated_event)
        elif event['id'] == event_id:  # this mean we're deleteing
            calendar.pop(index)

    # update calendar.json:
    f = open('calendar.json', 'w')
    json.dump(calendar, f, indent=2)
    f.close()


def get_event_id_and_availibility(calendar, date_time):
    """Checks and returns the avialiility"""
    
    for event in calendar:
        if event['start_time'] == date_time:
            return event['id'], event['summary'] == 'Availble Session'


def book_session(service, email, username):
    """Handles the booking a slot functionlity"""
    
    calendar_data = get_calendar_data()
    if calendar_data:
        choice = get_slot_to_cancel(calendar_data, username)

        slot = calendar_data[choice-1]
        availble = slot['summary'] == 'Availble Session'

        if availble:  # this means session can be booked
            desc = get_description(username)

            event = service.events().get(calendarId=get_calendar_id(),
                                         eventId=slot['id']).execute()
            event['summary'] = 'Unavaible Session'
            event['attendees'].append(
                {'email': f'{email}', 'responseStatus': 'needsAction'})
            event['description'] = desc

            updated_event = service.events().update(calendarId=get_calendar_id(),
                                                    eventId=event['id'], body=event).execute()
            update_calendar(
                calendar_data, slot['id'], updated_event=updated_event)

            # Print the updated date.
            print(f'{get_output_prefx(username)}Slot has been booked!')
            updated_event = structure_event_info(updated_event)
            display_event_data(updated_event, flag2=True)
        else:
            print(
                f"{get_output_prefx(username)}Error! Cannot book a slot that's already been booked.")
    else:
        print(f"{get_output_prefx(username)}No Slots Found")


def get_start_and_end_time(username, date):
    """Returns the start and end time of a slot"""

    time_slots = get_availble_time_slots(date)
    print(f"{get_output_prefx(username)}Choose A Time Slot From The Following:\n")

    for i, time in enumerate(time_slots):
        if i != 0:
            end_time = time + timedelta(minutes=30)
            print(f"\t\t\t {i}. {time.time()} - {end_time.time()}")

    time_index = input(f"{get_output_prefx(username)}Enter the number: ")
    start_time = time_slots[int(time_index)]
    end_time = (start_time + timedelta(minutes=30)).time()
    start_time = start_time.time()

    return start_time, end_time


def get_date(username):
    """Gets and Return the date from the user"""
    
    days = next_seven_days()

    # get the day
    print(f"{get_output_prefx(username)}Choose A Day From The Following:\n")
    for i, day in enumerate(days):
        if i != 0:
            print(f"\t\t\t {i}. {day}")
 
    day = ''
    while not day.isdigit() or day not in '1234567':
        day = input(f"{get_output_prefx(username)}Enter the number: ")

    return days[int(day)]


def return_datetime(date, time):
    """Returns the datetime"""
    return datetime(date.year, date.month, date.day, time.hour-2, time.minute, time.second)


def return_iso_string(date_time):
    """Returns the datetime in a iso string format"""
    return f'{date_time.isoformat()}Z'


def volunteer_session(service, username, email):
    """Handles all the volunteering for a time slot functionality."""

    date = get_date(username)
    start_time, end_time = get_start_and_end_time(username, date)

    start_datetime = return_datetime(date, start_time)
    end_datetime = return_datetime(date, end_time)

    start_datetime = return_iso_string(start_datetime)
    end_datetime = return_iso_string(end_datetime)

    event = create_event(email, start_datetime, end_datetime)
    
    confirmation = ''
    while confirmation not in ['y', 'n']:
        confirmation = input(f"{get_output_prefx(username)}\
Please confirm that you want to book a slot from {start_time} to {end_time} (y/n): ").lower()

    if confirmation == 'y':
        event_service = service.events().insert(
                        calendarId=get_calendar_id(), body=event).execute()
        if event_service:
            print(f"{get_output_prefx(username)}\
You've successfully volunteered for a timeslot.")
        else:
            print(f"{get_output_prefx(username)}An error occurred")
    else:
        print(f"{get_output_prefx(username)}Goodbye!")


def get_slot_to_cancel(calendar_data, username):
    """Handles getting the slot ro cancel or bookj from user"""
    
    print(f"{get_output_prefx(username)}Choose A Slot From The Following:\n")
    for i, event in enumerate(calendar_data):
        print(f"\t{i+1}.", end=" ")
        display_event_data(event, flag=True)
        
    choice = '-1'
    while not choice.isdigit() or (choice < '1' or choice > str(len(calendar_data))):
        choice = input(f"{get_output_prefx(username)}Enter the number: ")

    return int(choice)


def cancel_volunteering_session(service, email, username):
    """Handles the cancelling a volunteer slot fuctionality"""
    
    calendar_data = get_calendar_data()
    if calendar_data:
        choice = get_slot_to_cancel(calendar_data, username)

        slot = calendar_data[choice-1]
        availble = slot['summary'].lower() == 'availble session'

        # this means student has not booked session.
        if availble and slot['volunteer'] == email:
            # Delete event from google calendar
            service.events().delete(calendarId=get_calendar_id(),eventId=slot['id']).execute()
            update_calendar(calendar_data, slot['id'])

            print(
                f'{get_output_prefx(username)}Your volunteer session has been deleted!')
        else:  # this means student has booked
            print(f'{get_output_prefx(username)}Error, Cannot Delete!!! \
Either the slot has already been booked or this is not your slot.')
    else:
        print(f"{get_output_prefx(username)}No Slots Found")


def cancel_booking(service, email, username):
    """Handles the cancelling of a booking functionality"""
    
    calendar_data = get_calendar_data()

    if calendar_data:
        choice = get_slot_to_cancel(calendar_data, username)
        slot = calendar_data[choice-1]
        student_username = get_student_username(slot)
        student_email = return_email(student_username)

        # First retrieve the event from the API.
        if student_email == email:
            event = service.events().get(calendarId=get_calendar_id(),
                    eventId=slot['id']).execute()

            event['summary'] = 'Availble Session'
            # remove student from attendees
            for obj in event['attendees']:
                if email in obj.values():
                    event['attendees'].remove(obj)
            # remove student description
            event['description'] = "Tutoring Session"
            # update event
            updated_event = service.events().update(calendarId=get_calendar_id(),
                            eventId=event['id'], body=event).execute()

            if updated_event:
                update_calendar(
                    calendar_data, slot['id'], updated_event=updated_event)
                print(f"{get_output_prefx(username)}Booking has been cancelled.")
            else:
                print(f"{get_output_prefx(username)}An error Occurred!")
        else:
            print(
                f"{get_output_prefx(username)}Cannot unbook another student's slot.")
    else:
        print(f"{get_output_prefx(username)}No Slots Found")


def refresh_calendar_token():
    """Refreshes the codeclinic calendar token"""
    
    with open('calendar_token.json') as f:
        token_info = json.load(f)
    refreshToken(token_info['client_id'], token_info['client_secret'],
                 token_info['refresh_token'], token="calendar_token.json")


def refresh_user_token():
    """Refreshs the user's personal calendar token"""
    
    if os.path.exists('token.json'):
        with open('token.json') as f:
            token_info = json.load(f)
        refreshToken(token_info['client_id'], token_info['client_secret'],
                     token_info['refresh_token'], token="token.json")


def get_service(calendar=False):
    """Get the service"""
    
    creds = (
        create_token() if not calendar else 
        create_token(token='calendar_token', credentials='code_clinic/clinic_credentials.json')
        )
    try:
        service = build('calendar', 'v3', credentials=creds)
    except HttpError as error:
        print(f'An error occurred ${error}')
    return service
    
    
def setup_code(username):
    """Code that setup the fuctioning of the app"""

    creds = create_token() 
    email = return_email(username)
    home_dir = os.path.expanduser('~')
    user_config_file = f'{home_dir}/.userconfig.json'
    
    if not os.path.exists(user_config_file):
        set_calendar_access_rule(email)
    # refresh tokens
    refresh_calendar_token()
    refresh_user_token()
    try:
        service = build('calendar', 'v3', credentials=creds)
        store_next_seven_days(service)
        store_personal_calendar(service)
    except HttpError as error:
        print(f'Oops! An error occurred ${error}')
    
    return service


def help_menu():
    """Returns the 'help' menu"""
    return ("""\npython3 codeclinic.py [COMMAND]:\n\nValid Commands:
view_calendar or vc  - Shows the student's personal calendar and the codeclinic calendar.
volunteer - Volunteer for a time slot.
book - book a tome slot.
cancel_booking or cb - Cancel a booking.
cancel_volunteering - Cancel a your
Type 'q' to quit.\n""")


def main(username, email):
    """Handle the main flow of the program"""

    try:
        service = setup_code(username)
        action = get_action(username)

        # programe logic
        if action == 'volunteer session' or action == "3":
            volunteer_session(service, username, email)
        elif action == 'view calendar' or action == "1":
            view_calendar(service)
        elif action == 'book session' or action == "2":
            book_session(service, email, username)
        elif action == 'cancel booking' or action == "4":
            cancel_booking(service, email, username)
        elif action == 'cancel volunteer' or action == "5":
            cancel_volunteering_session(service, email, username)
        elif action == 'help':
            print(help_menu())
        elif action == 'q':
            quit()

    except HttpError as error:
        print(f'An error occurred ${error}')