import random


def generate_code():
    """Generate a four-digit code between 1-8 (inclusive) and tells the user that the code has been loaded.
    Returns:
        list: a list with 4 int elements.
    """
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    return code


def get_user_code():
    """Promps user for input and checks if format is correct.
    Returns:
        str: user_code as a string.
    """
    user_code = input("Input 4 digit code: ")
    while not user_code.isdigit() or len(user_code) != 4 or '0' in user_code or '9' in user_code:
        print("Please enter exactly 4 digits.")
        user_code = input("Input 4 digit code: ")
    return user_code


def check_answer(code, answer):
    """Checks how many numbers in answer are in the correct position and how many are in the code. Then displays it to the user.
    Returns:
        tuple: orrect_digits_and_position, orrect_digits_only.
    """
    correct_digits_and_position = 0
    correct_digits_only = 0
    
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1
    
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))     
    return correct_digits_and_position, correct_digits_only


def has_user_won(correct_pos, turns):
    """Checks if the user has won.
    Returns: Boolean
    """
    if correct_pos == 4:
        print('Congratulations! You are a codebreaker!')
        return True
    else:
        print('Turns left: '+str(12 - turns))
        return False


def run_game():
    """Runs the game.
    """
    code = generate_code()
    correct = False
    turns = 0
    while not correct and turns < 12:
        answer = get_user_code()
        correct_digits_and_position, _ = check_answer(code, answer) 
        turns += 1
        correct = has_user_won(correct_digits_and_position, turns)
    print('The code was: '+str(code))


if __name__ == "__main__":
    run_game()