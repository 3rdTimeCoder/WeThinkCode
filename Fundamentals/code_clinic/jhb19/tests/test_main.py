import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import codeclinic
import myCal


class MyTestCase(unittest.TestCase):
    def test_help_menu(self):
        ...
        help_menu = myCal.help_menu()
        self.assertEqual(help_menu, """\npython3 codeclinic.py [COMMAND]:\n\nValid Commands:
view_calendar or vc  - Shows the student's personal calendar and the codeclinic calendar.
volunteer - Volunteer for a time slot.
book - book a tome slot.
cancel_booking or cb - Cancel a booking.
cancel_volunteering - Cancel a your
Type 'q' to quit.\n""")
        

    def test_return_email(self):

        return_email = myCal.return_email('nkkhoza022')
        self.assertEqual(return_email, 'nkkhoza022@student.wethinkcode.co.za')

        return_email = myCal.return_email('nosifan022')
        self.assertEqual(return_email, 'nosifan022@student.wethinkcode.co.za')

        return_email = myCal.return_email('phmudau022')
        self.assertEqual(return_email, 'phmudau022@student.wethinkcode.co.za')

    
    def test_get_calendar_id(self):

        get_calendar_id = myCal.get_calendar_id()
        self.assertEqual(get_calendar_id, 'jhb19.wethinkcode@gmail.com')
        

    def test_get_action(self):

        with captured_io(StringIO("1\n")) as (out,err):

            myCal.get_action('nkkhoza022')
        output = out.getvalue().strip()
        self.assertTrue(output.find("Select An Option From Below...\n\n \t\t1. view calendar\n \t\t2. book session\n \t\t3. volunteer session\n \t\t4. cancel booking\n \t\t5. cancel volunteer session\n"))
    
    
    def test_get_description(self):

        with captured_io(StringIO("functions and algorithms\n")) as (out,err):

            result = myCal.get_description('nkkhoza022')
        self.assertEqual("functions and algorithms", result)
        
        
    def test_get_student_username_booked(self):
        event = {
                    "volunteer": "nosifan022@student.wethinkcode.co.za",
                    "attendees": [
                    {
                        "email": "jhb19.wethinkcode@gmail.com",
                        "organizer": True,
                        "self": True,
                        "responseStatus": "needsAction"
                    },
                    {
                        "email": "nosifan022@student.wethinkcode.co.za",
                        "responseStatus": "needsAction"
                    },
                    {
                        "email": "phmudau022@student.wethinkcode.co.za",
                        "responseStatus": "needsAction"
                    }
                    ],
                }
        results = myCal.get_student_username(event) 
        
        self.assertEqual(results,"phmudau022")   
        
        
    def test_get_student_username_other_booked(self):
        event = {
                    "volunteer": "nosifan022@student.wethinkcode.co.za",
                    "attendees": [
                    {
                        "email": "jhb19.wethinkcode@gmail.com",
                        "organizer": True,
                        "self": True,
                        "responseStatus": "needsAction"
                    },
                    {
                        "email": "nosifan022@student.wethinkcode.co.za",
                        "responseStatus": "needsAction"
                    },
                    {
                        "email": "nkkhoza022@student.wethinkcode.co.za",
                        "responseStatus": "needsAction"
                    }
                    ],
                }
        results = myCal.get_student_username(event) 
        
        self.assertEqual(results,"nkkhoza022")     
        
         
    def test_get_student_username_not_booked(self):
        event = {
                    "volunteer": "nosifan022@student.wethinkcode.co.za",
                    "attendees": [
                    {
                        "email": "jhb19.wethinkcode@gmail.com",
                        "organizer": True,
                        "self": True,
                        "responseStatus": "needsAction"
                    },
                    {
                        "email": "nosifan022@student.wethinkcode.co.za",
                        "responseStatus": "needsAction"
                    },
                    ],
                }
        results = myCal.get_student_username(event) 
        
        self.assertEqual(results,"-")           

if __name__ == '__main__':
    unittest.main()
