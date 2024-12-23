# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 19:58:57 2024

@author: KIIT0001
"""

command = ""
started = False
helped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started: 
            print("car is already started, numbskull!!!")
        else:
            started = True
            print("The car is started and ready to go!")
    elif command == "stop":
        if not started:
            print("the car is aready stopped, moron!!!")
        else:
            started = False
            print("the car is stopped now for good")
    elif command == "help":
        print("""
start - to start the car
stop -  to stop the car
quit - to quit the game
help -  to see the commands
        """)
    elif command == "quit":
        break
    else:
        print("what are you typing you illiterate piece of shi- i mean cake!!!")
        
            