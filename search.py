# Imports

from datetime import datetime
from speeds import fast_text, wait_text
from text_colours import *

def search_a(time):
    answers=["1","2","3","4"]
    fast_text("Initiating Search \n\n")
    fast_text(f"{bcolors.WARNING}Search system currently semi-operational \nPlease build search modularly{bcolors.ENDC} \n\nPlease input your search term\n")
    ans1=input("      >>    ")
    fast_text("Please wait - search building\n")
    wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
    print(f" {bcolors.OKGREEN} if {ans1} in {bcolors.ENDC}")
    fast_text("Where are you searching? \nSelect from the following options: \n\n 1 - System Log \n 2 - System Settings \n 3 - User Database \n 4 - Asset Catalogue \n\n Please type 1, 2, 3 or 4")
    ans2=input("      >>    ")

    while ans2 not in answers:
        fast_text(f"{bcolors.WARNING}Unexpected input \n Please Try Again {bcolors.ENDC} \n Please type 1, 2, 3 or 4")
        ans2=input("      >>    ")


    if ans2=="1":
        search_place="System Log"
        print(f" {bcolors.OKGREEN} if {ans1} in {search_place} {bcolors.ENDC}")
        print(f" {bcolors.OKGREEN}      print(all_occurences()) {bcolors.ENDC}\n \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"Searching for {ans1} in the {search_place} \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"{bcolors.OKCYAN} 2 matching item(s) found in System Log{bcolors.ENDC}")
        our_search=datetime.datime.now()
        print(f"""
<aa0Exffdo> System clear 300622 11:57:30.76821
<aa0Exffdo> System clear 300622 13:57:30.18236
<aa0Exffdo> System clear 300622 15:57:30.40923
{bcolors.OKCYAN}<aa0ExSEARCH_USER_DB()> "090477" at {time} {bcolors.ENDC}
{bcolors.OKCYAN}<aa0ExSEARCH_SYS_LOGS()> "090477" at {our_search} {bcolors.ENDC}

""")
        fast_text("What would you like to do now? \n\n1 - Search Again? \n2-Quit Search? \n Please type 1 or 2\n")
        again=input("      >>    ")
        while again !="1" and again !="2":
            fast_text(f"{bcolors.WARNING}Unexpected input \n Please Try Again {bcolors.ENDC} \n Please type 1 or 2")
            again=input("      >>    ")

        if again=="1":
            search_a(time)
        else:
            return

    elif ans2=="2":
        print(f"Searching for {ans1} in the System Settings \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        print(f"Found 1 instance of {ans1} - password changed at {time}")
    elif ans2=="3":
        print(f"Searching for {ans1} in the User Database \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        print(f"Found 1 instance of {ans1}")
    elif ans2=="4":
        print(f"Searching for {ans1} in the Asset Catalogue \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        print(f"Found 1 instance of {ans1}")


# if ans2=="1"