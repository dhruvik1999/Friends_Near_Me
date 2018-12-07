from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Details,FriendObj
import json
import urllib.request
import os
from pprint import pprint
from math import sin ,cos,sqrt,atan2,radians
# Create your views here.

def index(request):

    friend_user_details=FriendObj.objects.all()
    return render(request,'index.html',{'friend_users':friend_user_details})


def findFriend(request):
    data=[]
    try:
        with urllib.request.urlopen("https://gist.githubusercontent.com/mishal23/ce4e164fea5bacb21d10970b9b8555af/raw/ab35e62c3a726924f703b7b6a8e7317ada002c66/friends.json") as url:
            data = json.loads(url.read().decode())
    except Exception as e:        
        print("Connection Error : Please Check The Connection") 
        FriendObj.objects.all().delete()  
        #print(data)
    try:
        lat=request.POST['ip_lat']
        x1=float(lat)
        lon=request.POST['ip_lon']
        y1=float(lon)
        dist=request.POST['ip_dist']
        z=float(dist)
        FriendObj.objects.all().delete()
        for item in data:
            x2=float(item['latitude'])
            y2=float(item['longitude'])


            dlon=x2-x1
            dlat=y2-y1
            dlon=radians(dlon)
            dlat=radians(dlat)
            a=sin(dlat/2)**2 + cos(x1)*cos(x2)*sin(dlon/2)**2
            c=2*atan2(sqrt(a),sqrt(1-a))
            d=c*6373

            if d<=z:
                a=FriendObj(latitutude=item['latitude'],longitude=item['longitude'],user_id=item['user_id'],name=item['name'])
                a.save()
    except FloatingPointError:
        print("Please enter floating point values")
    return HttpResponseRedirect('/search/')