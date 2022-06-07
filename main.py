#######################################
#                                     #
#          local imports              #
#                                     #
#######################################

from password import login,login_stamp
from search import search_a
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

start_stamp=datetime.datetime.now()
ans=["1","2","3","4","5","6"]

#######################################
#                                     #
#          function order             #
#                                     #
#######################################

def options():
    fast_text(f"Please select from the following options: \n   1 - Access Asset Catalogue \n   2 - Access User Database\n   3 - Access System Settings \n   4 - Search System \n   5 - Access Server Management Tools \n   6 - Quit \nPlease input 1,2,3 or 4. Press 6 to quit")
    main_option=input("     >>    ")

    while main_option not in ans:
        fast_text(f"{bcolors.WARNING}Unexpected input \nPlease Try Again {bcolors.ENDC} \nPlease type 1, 2, 3 or 4. Press 6 to quit.")
        main_option=input("     >>    ")

    if main_option=="1":
        print("for now")
    elif main_option=="2":
        print("for now")
    elif main_option=="3":
        login()# the login puzzle
        fast_text("What would you like to do? \n")
        options()
    elif main_option=="4":
        search_a(start_stamp) # the searching
        fast_text("What would you like to do? \n")
        options()



fast_text(f"{bcolors.HEADER}         Welcome To\n Liverpool Central Library Server Management {bcolors.ENDC}\n\n")
fast_text("Please enter the password\n")
password=input("     >>    ")
while password !="090477":
    fast_text(f"{bcolors.FAIL}Incorrect, please try again \nYou have 999 tries remaining {bcolors.ENDC}\n")
    password=input("     >>    ")

wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
print(f"{bcolors.OKGREEN} Access Granted \n \n Welcome Admin {bcolors.ENDC}\n\n")
options()