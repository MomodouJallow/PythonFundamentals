## PLEASE STUDY THIS CODE(a note to myself)
is_started = False
while True:
    cursor = input(">").upper()
    if cursor == "HELP":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif cursor == "START":
        if is_started:
            print("Car is already started!")
        else:
            is_started = True
            print("Car started...Ready to go!")
    elif cursor ==  "STOP":
        if not is_started:
            print("Car already stopped!")
        else:
            is_started = False
            print("Car stopped.")
    elif cursor == "QUIT":
        break
    else:
        print("I don't understand that...")
