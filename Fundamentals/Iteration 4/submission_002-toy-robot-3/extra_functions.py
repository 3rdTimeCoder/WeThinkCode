def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def help_menu():
    """Returns the 'help' menu"""
    return ("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - moves robot forward. i.e. 'forward 10' moves robot forward by 10 steps.
BACK - moves robot back. i.e. 'back 10' moves robot back by 10 steps.
RIGHT - turns robot to the right by 90 degrees.
LEFT - turns robot to the left by 90 degrees.
SPRINT - sprints robot forward by given steps.
REPLAY - replays all the movement commands you've typed thus far.
REPLAY SILENT - replays history silently.
REPLAY REVERSED - replays history in reverse.
REPLAY REVERSED SILENT - replays history in reverse silently.\n""")