#######################################
#                                     #
#          local imports              #
#                                     #
#######################################

from speeds import fast_text, wait_text
from text_colours import *

#######################################
#                                     #
#          library imports            #
#                                     #
#######################################

import datetime

#######################################
#                                     #
#          variables                  #
#                                     #
#######################################

pin="090477"
done_before=False
login_stamp=datetime.datetime.now()

#######################################
#                                     #
#          function start             #
#                                     #
#######################################

def login():
    global pin, done_before
    fast_text("Sys Login: \n")
    log_pin=input("     >>    ")


    while log_pin !=pin:
        fast_text(f"{bcolors.FAIL}Incorrect, please try again \nYou have 999 tries remaining {bcolors.ENDC}\n")
        log_pin=input("")
    
    if done_before:
        return
    
    fast_text(f"{bcolors.WARNING}**WARNING** \n Changes made here will impact the whole system \n You may need to log in again\n {bcolors.ENDC}")

    fast_text(f" System Settings \n What would you like to do? \n ")
    fast_text("filler options    select 6 to change password")
    sys_setting_options=input("")

    if sys_setting_options=="6":
        fast_text(f"{bcolors.WARNING}**WARNING** \n Changes made here will impact the whole system \n You may need to log in again\n {bcolors.ENDC}")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"{bcolors.WARNING}Accessing System Root Password Settings \n Current Permissions: \n{bcolors.ENDC}")
        print(f"""{bcolors.OKGREEN} if password=="{pin}:
                allow_access(True) {bcolors.ENDC}""")
        fast_text("What would you like to change the password to?")
        new_pin=input("")
        fast_text("Please confirm the pin")
        new_pin_again=input("")
        while new_pin != new_pin_again:
            fast_text(f"{bcolors.FAIL} ***ERRORR** pins did not match \n {bcolors.ENDC}")
            fast_text("What would you like to change the password to?")
            new_pin=input("")
            fast_text("Please confirm the pin")
            new_pin_again=input("")

        if new_pin==new_pin_again:
            pin=new_pin
            fast_text(f"{bcolors.OKGREEN} You have successfully changed the password {bcolors.ENDC} \n")
            fast_text("Please log in again with the new password")
            done_before=True
            login()

login() # remember to comment out this line when going back to main.py