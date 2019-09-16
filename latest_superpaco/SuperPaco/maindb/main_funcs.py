from datetime import datetime,timedelta
from hashlib import sha256
from typing import List
from .models import *

import timestring
import json

def get_folder():
    """
    Function which returns the name of the folder of the back ups


    (To shorten the work if something needs to be done with the CSV data)
    """

    date = datetime.now()
    folder = f"back/{date.year}/{date.month}.{date.strftime('%B')}/{date.year}-{date.month}-{date.day}/"
    return folder

"""
General functions for multi-use
"""

def update_object(obj: object,args: List[str],values: List[str],*,type: str):
    """
    Function for updating the object first in local memory, then
    in the database
    """

    for attr,val in zip(args,values):
        if attr in ['good_choices','bad_choices']:
            tmp_val = dict(obj)[attr]
            tmp_val += val
        elif attr in ['choices']:
            tmp_array = dict(obj)[attr]
            tmp_array.append(val)
            tmp_val = tmp_array
        else:
            tmp_val = val
        setattr(obj, attr, tmp_val)

    obj.save(update_fields=args)

def prevent_DDOS(user_obj: object):
    """
    Function which updates the times of use of the game,
    and, if there were more than 4 requests to the server/database
    in a timespan of 60 seconds, deny the request
    """

    try:
        timer = []
        user_obj.time_stamps.append(str(datetime.now()))
        """
        Collect time differences from last 4 requests in a list
        """
        if len(user_obj.time_stamps) > 4:
            for xn in range(1,5):
                timer.append(timestring.Date(user_obj.time_stamps[-xn]).date - timestring.Date(user_obj.time_stamps[-xn-1]).date)
                
            final = timedelta()

            """
            Sum the differences up
            """

            for xn in timer:
                final += xn

            """
            Deny the request if the difference was smaller than 60 seconds
            """

            if(final < timedelta(seconds=60)):
                return(False)

            return True

    except:
        return False

"""
Main functions
"""

def create_users(request):
    """
    Function that gives a certain hash to a new user, and then keeps it stored,
    while checking whether the IP adress has already been used
    """

    temp = sha256(request.META['REMOTE_ADDR'].encode('utf-8')).hexdigest()
    user = User.objects.get_or_create(user_hash = temp)
    update_basic_fields(request,user)
    return(temp)


def update_choice_fields(request):
    """
    Updates the user's choices in-game
    """

    req = json.loads(request.body)
    allowed_fields = ["id", "good_choices", "bad_choices", "choices"]
    if req.keys() == allowed_fields:
        try:
            user_obj = User.objects.get(user_hash = req['id'])
        except:
            return False


        if not prevent_DDOS(user_obj):
            return False

        update_object(user_obj,req.keys(),req.values(),type="update_choices")

        user_obj.save(update_fields=req.keys())
        return(True)

    else:
        return False
    

def update_basic_fields(request,tmp_obj: User = None):
    """
    Function which updates the user's basic info, should be probably implemented inside of the make() function
    """

    req = json.loads(request.body)
    allowed_fields = {
        'age' : 'godini',
        'gender' : 'gender',
        'q1' : 'zrtva_na_nasilstvo',
        'q2' : 'svedok_na_nasilstvo'
        }
    if req.keys() == allowed_fields.values():
        try:
            if tmp_obj == None:
                user_obj = User.objects.get(user_hash = req['id'])
            else:
                user_obj = tmp_obj
        except:
            return False

        update_object(user_obj,allowed_fields.keys(),req.values(),type="updating_basic_info")
            
        z.save(update_fields=allowed_fields.keys())
            
        return(True)

    else:
        return(False)


"""
Dumps
"""


def dump():
    """
    Function which dumps the data of inactive users to a 'default' model
    where they are kept/stored
    """

    set1 = User.objects.filter(activity=False)
    leftovers = Leftovers.objects.get(name='leftovers')

    for i in set1:
        leftovers.good_choices += i.good_choices
        leftovers.neutral_choices.append(i.choices)
        leftovers.bad_choices += i.bad_choices
    
    set1.delete()
    
def dump_timer():
    """
    Recursive function: Counter for when to activate dump()
    """

    dump_day = dt.today().month + 1
    while True:
        if dt.today().month == dump_day:
            dump()
            dump_timer()
        time.sleep(86400)


"""
Back up
"""

def back_up_timer():
    """
    Recursive function: Counter for when to activate back()
    """
    day = dt.today().day + 1
    while True:
        if dt.today().day == dump_day:
            back_up()
            back_up_timer()
        time.sleep(86400)

def back_up():
    """
    Function which back's up the models in the database to a CSV file
    """

    folder = get_folder()
    try:
        os.makedirs(folder)
    except:
        pass

    User.objects.to_csv(folder + "users.csv",encoding='utf-8')
