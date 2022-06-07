# Imports
import datetime
from speeds import fast_text, wait_text
from text_colours import *

def search_a(time):
    answers=["1","2","3","4"]
    fast_text("Initiating Search \n\n")
    fast_text(f"{bcolors.WARNING}System Search currently semi-operational \nPlease build search modularly{bcolors.ENDC} \n\nPlease input your search term\n")
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
        our_search=datetime.datetime.now()
        print(f"""
<aa0Exffdo> System clear 300622 11:57:30.76821
<aa0Exffdo> System clear 300622 13:57:30.18236
<aa0Exffdo> System clear 300622 15:57:30.40923
{bcolors.OKCYAN}<aa0ExSEARCH_USER_DB()> "090477" at {time} {bcolors.ENDC}
{bcolors.OKCYAN}<aa0ExSEARCH_SYS_LOGS()> "090477" at {our_search} {bcolors.ENDC}

""")
        fast_text("What would you like to do now? \n\n1 - Search Again? \n2 - Quit Search? \n Please type 1 or 2\n")
        again=input("      >>    ")
        while again !="1" and again !="2":
            fast_text(f"{bcolors.WARNING}Unexpected input \n Please Try Again {bcolors.ENDC} \n Please type 1 or 2")
            again=input("      >>    ")

        if again=="1":
            search_a(time)
        else:
            return

    elif ans2=="2":
        search_place="System Settings"
        print(f" {bcolors.OKGREEN} if {ans1} in {search_place} {bcolors.ENDC}")
        print(f" {bcolors.OKGREEN}      print(all_occurences()) {bcolors.ENDC}\n \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"Searching for {ans1} in the {search_place} \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"{bcolors.OKCYAN}1 matching item(s) found in System Settings{bcolors.ENDC}\n")
        print(f"""pass_log: Unkown User set_password({bcolors.OKCYAN} "090477"{bcolors.ENDC} at {time})
""")
        fast_text("What would you like to do now? \n\n1 - Search Again? \n2 - Quit Search? \n Please type 1 or 2\n")
        again=input("      >>    ")
        while again !="1" and again !="2":
            fast_text(f"{bcolors.WARNING}Unexpected input \n Please Try Again {bcolors.ENDC} \n Please type 1 or 2")
            again=input("      >>    ")

        if again=="1":
            search_a(time)
        else:
            return

    elif ans2=="3":
        search_place="User Database"
        print(f" {bcolors.OKGREEN} if {ans1} in {search_place} {bcolors.ENDC}")
        print(f" {bcolors.OKGREEN}      print(all_occurences()) {bcolors.ENDC}\n \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"Searching for {ans1} in the {search_place} \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        fast_text(f"{bcolors.OKCYAN}4 matching item(s) found in System Settings{bcolors.ENDC}\n")

        print(f"""
        {bcolors.WARNING}Name:{bcolors.ENDC} Batey, Stephen    {bcolors.WARNING}User Number:{bcolors.ENDC} LCC0374992     {bcolors.WARNING}Current:{bcolors.ENDC} 0 pending    {bcolors.WARNING}Notes:{bcolors.ENDC} N/A
        {bcolors.WARNING}Name:{bcolors.ENDC} Davies, Kieran    {bcolors.WARNING}User Number:{bcolors.ENDC} LCC0600345     {bcolors.WARNING}Current:{bcolors.ENDC} 2 pending    {bcolors.WARNING}Notes:{bcolors.ENDC} N/A
        {bcolors.WARNING}Name:{bcolors.ENDC} Gregor, James     {bcolors.WARNING}User Number:{bcolors.ENDC} LCC0998947     {bcolors.WARNING}Current:{bcolors.ENDC} Banned       {bcolors.WARNING}Notes:{bcolors.ENDC} {bcolors.FAIL}7 Unreturned - MAX FINE{bcolors.ENDC}
        {bcolors.WARNING}Name:{bcolors.ENDC} Traynor, Mary     {bcolors.WARNING}User Number:{bcolors.ENDC} LCC0967783     {bcolors.WARNING}Current:{bcolors.ENDC} 7 pending    {bcolors.WARNING}Notes:{bcolors.ENDC} Pre-order BIThalo
""")
        fast_text("What would you like to do now? \n\n1 - Search Again? \n2 - Quit Search? \n Please type 1 or 2\n")
        again=input("      >>    ")
        while again !="1" and again !="2":
            fast_text(f"{bcolors.WARNING}Unexpected input \n Please Try Again {bcolors.ENDC} \n Please type 1 or 2")
            again=input("      >>    ")

        if again=="1":
            search_a(time)
        else:
            return
    elif ans2=="4":
        print(f"Searching for {ans1} in the Asset Catalogue \n")
        wait_text(f"{bcolors.OKBLUE}. . .{bcolors.ENDC}\n")
        print(f"Found 1 instance of {ans1}")

search_a(4)