#######################################
#                                     #
#          local imports              #
#                                     #
#######################################

from password import login,login_stamp
from search import search_a

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

#######################################
#                                     #
#          function order             #
#                                     #
#######################################

login() # the login puzzle
print(login_stamp) # printing stamp as proof of time capture
search_a(start_stamp) # the searching 
print("fin") # cocde to prove return is working