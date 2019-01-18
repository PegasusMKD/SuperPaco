import json

from ..models import ID
from django.http import HttpResponse   


#Sozdava nov "user"

def make(request):

    temp = request.META['REMOTE_ADDR']          #Zema IP
    a = []                                                                     #H
    for i,y in zip(str(temp.split('.')),range(len(str(temp.split('.'))))):     #A
        if y / 2 == 0:                                                         #S
            a.append(chr(int(ord(i)) * 2 + 2))                                 #H
        else:                                                                  #I
            a.append(chr(int(ord(i)) + 12 ))                                   #N
    user_id = ''.join(a)                                                       #G
    
    
   
   
   
   #Prva proverka, dali ima isti ID, bez oznakata za pk

    if user_id in [x.id_m[0:len(user_id)] for x in ID.objects.all()]:
        z = ID.objects.all()                                 #Prvichna verzija bez filter, bidejki, filterot
                                                            #ide na premnogu precizni vrednosni, odnosno, od character za character
                                                            #mora da se poklapaat

        used = [x.id_m for x in z if user_id == x.id_m[0:len(user_id):1]]
        temp = used[-1]
    
#Da se dvizhi i nagore po listata, i nadole

        #if int(temp[-1]) - 1 != 0 and (user_id + str(int(temp[-1]) - 1)) not in used:
        #    user_id_new = user_id + str(int(temp[-1]) - 1)
        #elif:
        num = temp[-1:-3:-1]
        user_id_new = user_id + "0" + str(int(num[::-1]) + 1)
        
#Povikuva nova varijabla so klasata, i i zaddava imot

        b = ID(id_m = user_id_new)
        b.save()
        print("Part 1\n User:" + b.id_m)
        return(user_id_new) #check(request)

    #Chisto debugging 

    elif user_id is None:
        if temp is None:
            print("Not taking in the IP")
        else:
            print("It's something else!")

    #Dokolku ne postoi, a i nema problemi pri hashing, napravi novo

    else:
        b = ID(id_m = user_id + "01")
        b.save()
        print("Part 2\n User:" + b.id_m)
        return(b.id_m) #check(request)

#Proveruva dali postoi, i, ako postoi, dodava na podatocite

def check(request):
    if request.META['CONTENT_TYPE'] == 'application/json':
        user_id = json.loads(request.body)
        if ID.objects.filter(id_m = user_id['id']).exists():
             #and type(int(user_id['good_choices'])) is int and type(int(user_id['bad_choices'])) is int and type(int(user_id['neutral_choices'])) is int:
            
            try:
                int(user_id['good_choices'])
                try:
                    int(user_id['neutral_choices'])
                    try:
                        int(user_id['bad_choices'])
                    except ValueError:
                        return(HttpResponse("<h1>UwU</h1>"))
                except ValueError:
                    return(HttpResponse("<h1>UwU</h1>"))
            except ValueError:
                return(HttpResponse("<h1>UwU</h1>"))

            z = ID.objects.get(id_m = user_id['id'])
            z.good_choices += int(user_id['good_choices'])
            z.neutral_choices += int(user_id['neutral_choices'])
            z.bad_choices += int(user_id['bad_choices'])

            z.save()

            return(True)
    else:
        return(False)
        
def basic(request,a):
    if request.META['CONTENT_TYPE'] == 'application/json':
        user_id = json.loads(request.body)
        print(user_id)
        user_ip = request.META['REMOTE_ADDR']
        print("IP: " + user_ip)
        print("Value of a:" + a)
        if ID.objects.filter(id_m = a).exists() and '(' not in user_id['gender'] and '(' not in user_id['zrtva_na_nasilstvo'] and '(' not in user_id['svedok_na_nasilstvo']:
            try:
                int(user_id['godini'])
            except ValueError:
                return(False)

            z = ID.objects.get(id_m = a)
            z.gender = user_id['gender']
            z.age = int(user_id['godini'])
            z.q1 = user_id['zrtva_na_nasilstvo']
            z.q2 = user_id['svedok_na_nasilstvo']

            z.save()
            return(True)
        else:
            return(False)
    else:
        return(False)