from ..models import Leftovers, ID 
from datetime import datetime as dt

def dump():

    set1 = [x for x in ID.objects.all() if x.activity == False]
    leftovers = Leftovers.objects.get(name='leftovers')

    for i in set1:
        leftovers.good_choices += i.good_choices
        leftovers.neutral_choices += i.neutral_choices
        leftovers.bad_choices += i.bad_choices
    
    ID.objects.filter(activity = False).delete()
    
def time_check():
    dump_day = dt.today().month + 1
    while True:
        if dt.today().month == dump_day:
            dump()
            dump_day = dt.today().month + 1
            