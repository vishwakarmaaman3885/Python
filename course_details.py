import os ,sys
from os.path import dirname , join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

#from payment import payment_details

def course():
    print("this is my course file")

#payment_details.payment() 


# here i can access my payment details on course file

# packages is nothing but a directory or folder example- course,payment folder
# # and python file can as module- payment_details.py