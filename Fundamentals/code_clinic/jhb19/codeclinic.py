import os
import click
import json
from get_username import get_username
import myCal
from output_functions import *


@click.command()
@click.argument('command', default="login")
def main(command):
    service = myCal.get_service()
    username, email = get_user_details()
    myCal.setup_code(username)
    
    if command == "login":
        login()
    elif command in ["view_calendar", "vc"]:
        myCal.view_calendar(service)
    elif command == "volunteer":
        myCal.volunteer_session(service, username, email)
    elif command == "book":
        myCal.book_session(service, email, username)
    elif command in ["cancel_booking", "cb"]:
        myCal.cancel_booking(service, email, username)
    elif command in ["cancel_volunteering", "cv"]:
        myCal.cancel_volunteering_session(service, email, username)
    elif command == "help":
        print(myCal.help_menu())
    else:
        print(f'{get_output_prefx(username)}invalid command')


def login():
    """Logs user in to codeclinic"""
    username,email = get_user_details()
    clear_terminal()
    output(username, f"Hello!!! Welcome To CodeClinic!\n")
    myCal.main(username, email)
        

def output(username, message):
    click.echo(f"\n{get_output_prefx(username)}{message}")
    
    
def get_user_details():
    """Gets and Returns the username and email"""
    
    home_dir = os.path.expanduser('~')
    user_config_file = f'{home_dir}/.userconfig.json'
    
    if os.path.exists(user_config_file):
        file = open(user_config_file, 'r')
        file_content = json.loads(file.read())
        file.close()
        
        username = file_content["username"]
        email = file_content["email"]
        
        return username , email
    else:
        username = get_username()
        email = myCal.return_email(username)
        user_info = {
            "username" : username,
            "email" : email  
        }
        file = open(user_config_file, 'w')
        json.dump(user_info, file, indent=2)
        file.close()
        return username , email


def clear_terminal():
    os.system('clear')


if __name__ == '__main__':
    main()