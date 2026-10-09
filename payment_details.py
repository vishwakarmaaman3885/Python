import os ,sys
from os.path import dirname , join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))


from course import course_details

def payment():
    print("this is my paymnt file")

course_details.course()

# here i can access my course details on payment file