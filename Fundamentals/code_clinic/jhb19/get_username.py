def get_username():
    """Gets and Returns username from user"""
    
    while True:
        username = input("Enter your username: ")
    
        if username == " " or len(username) != 10 :
            continue
        elif not username[0].isalpha() or  not username[1].isalpha() or \
        not username[2].isalpha() or not username[3].isalpha() or not username[4].isalpha() \
        or not username[5].isalpha() or not username[6].isalpha():
            print("Invalid username!")
            continue
        elif not username[7].isdigit() or not username[8].isdigit() or not username[9].isdigit():
            print("Invalid username!")
            continue
        
        else:
            break
    return username