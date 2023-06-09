def create_event(email, start_time, end_time):
    """Creates and return an event object"""

    return {
        'summary': 'Availble Session',
        'location': 'WeThinkCode Joburg Campus',
        'description': 'Tutoring Session',
        'start': {
            'dateTime': start_time,
            'timeZone': 'Africa/Johannesburg',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Africa/Johannesburg',
        },
        'recurrence': ['RRULE:FREQ=DAILY;COUNT=1'],
        'attendees': [
            {'email': 'jhb19.wethinkcode@gmail.com', 'displayName' : 'codeclinic'},
            {'email': email},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
