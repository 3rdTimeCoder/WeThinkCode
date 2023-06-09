def testing(something):
    try:
        assert(type(something) == int)
        print(something + 10)
    except AssertionError as err:
        print("please enter an integer")
    
    
testing('50')