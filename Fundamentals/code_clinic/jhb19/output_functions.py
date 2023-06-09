import click


def bold_blue(string):
    return click.style(string, fg='blue', bold=True)


def bold_green(string):
    return click.style(string, fg='green', bold=True)


def normal_green(string):
    return click.style(string, fg='green')


def normal_blue(string):
    return click.style(string, fg='blue')


def get_output_prefx(username):
    """Adds standard prefix to output"""
    user_type_terminal_str = bold_green(f"({username})")
    jhb19 = bold_blue("jhb19")
    return f"\n{user_type_terminal_str}{jhb19}: "