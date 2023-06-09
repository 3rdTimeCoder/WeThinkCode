import random


def run_game():
    turns = 12
    code = ''
    while len(code) != 4:
        random_num = str(random.randint(1,8))
        if random_num not in code:
            code += random_num     
    print(code)

    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    # main game loop
    while turns > 0:
        turns -= 1
        correct_pos = 0
        correct_nums = 0
        
        # step 2
        user_code = input("Input 4 digit code: ")
        while not user_code.isdigit() or len(user_code) != 4 or '0' in user_code or '9' in user_code:
            print("Please enter exactly 4 digits.")
            user_code = input("Input 4 digit code: ")
        
        # step 3 - check correct numbers
        for index, num in enumerate(user_code):
            if code[index] == num:
                correct_pos += 1
            elif code[index] != num and num in code:
                correct_nums += 1
                 

        # give user feedback
        print(f"Number of correct digits in correct place:     {correct_pos}")
        print(f"Number of correct digits not in correct place: {correct_nums}")
        
        # check if user won game:
        if user_code == code:
            print("Congratulations! You are a codebreaker!")
            print(f"The code was: {''.join(code)}")
            break
        else:
            print(f"Turns left: {turns}")
    
    # check if player ran out of cahnces.
    if turns == 0:
        print("Sorry. You've run out of chances.")
    
    

if __name__ == "__main__":
    run_game()
