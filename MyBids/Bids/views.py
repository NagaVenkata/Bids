#from django.shortcuts import render
from Bids.models import User
from Bids.models import Items
from MyBids.settings import PROJECT_ROOT

from django.core.context_processors import csrf
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.core.exceptions import ValidationError
from django.shortcuts import render_to_response

from django_mongoengine.mongo_auth import models

import datetime
import os



# Create your views here.

# Login handles the user login 

def main(request):
    
    c={}
    
    #if (request.user.username) :
        
    #c.update(csrf(request))
    #c.update(username = request.user.username)
    #return render_to_response("home.html",c)
    
                
    #print (items[0].itemName)
                
    bidItems = []
                
    for item in Items.objects.all():
        items = {}
        items['name'] = item.itemName.encode('utf-8')
        items['type'] = item.itemType.encode('utf-8')
        items['Descp'] = item.itemDescp.encode('utf-8') 
        items['price'] = item.itemPrice
        items['image1'] = item.image1.encode('utf-8')
        items['posted'] = item.timestamp.strftime('%Y-%m-%d')
                    
                    
        bidItems.append(items) 
               
                
    print (bidItems)
                
    c.update(items = bidItems)
        
        
    return render_to_response("home.html",c)
    
def loginUser(request):
    
    c={}
    c.update(csrf(request))
     
    if request.method == "POST":
        
        
        users = User.objects.filter(email = request.POST['email'])
        
        print (users[0].name)
             
        if len(users) > 0:
            #user = authenticate(username = users[0].name, password = request.POST['password'])
            if users[0] is not None:
                #if user.is_active:
                #login(request,users[0]) 
                c.update(username = users[0].name)
                
                User.objects.all()
                
                items = Items.objects.all()
                
                #print (items[0].itemName)
                
                bidItems = []
                
                for item in Items.objects.filter(user=users[0]):
                    items = {}
                    items['name'] = item.itemName.encode('utf-8')
                    items['type'] = item.itemType.encode('utf-8')
                    items['Descp'] = item.itemDescp.encode('utf-8') 
                    items['price'] = item.itemPrice
                    items['image1'] = item.image1.encode('utf-8')
                    items['posted'] = item.timestamp.strftime('%Y-%m-%d')
                    
                    
                    bidItems.append(items) 
               
                
                print (bidItems)
                
                c.update(items = bidItems)
                
                return render_to_response("home.html",c)
             
        else:
            c.update(error = "Invalid username/password")
            return render_to_response("login.html",c)
            
    return render_to_response("login.html",c)

def logoutUser(request):
    
    #logout(request)   
        
    return render_to_response("home.html") 

def register(request):
    
    if request.method == "POST":
        user = User(name = request.POST['username'],
                    password = request.POST['password'], 
                    email = request.POST['email']
                    )
        user.save()
        return render_to_response("registerComplete.html")    
        
    c={}
    c.update(csrf(request))
    
    
    return render_to_response("register.html",c)    



def addItem(request):
    
    if request.method == "POST":
        
        print (request.POST['userName'])
        
        user = User.objects.get(name = request.POST['userName'])
        
        item_name = request.POST['itemName']
        item_type = request.POST['itemType']
        item_descp = request.POST['itemDescp']
        
        print (item_type)
         
#         print (request.POST['itemName'])
#         print (request.POST['itemType'])
#         print (request.POST['itemDescp'])
#         print (request.FILES.getlist('files'))
        
        filename = None
        
        for item in request.FILES.getlist('files'):
            filename = save_uploadImage(request.POST['userName'],item)
        
    
        
        item = Items(
                     user = user,
                     itemName = item_name,
                     itemType = item_type,
                     itemDescp = item_descp,
                     itemPrice = 200.0,
                     image1 = filename,
                     image2 = "",
                     image3 = "",
                     image4 = "",
                     timestamp = datetime.datetime.now())
           
        item.save()
                     
    c={}
    c.update(csrf(request))
    return render_to_response("home.html",c)

def save_uploadImage(username,imageFile):
    #Set Project Path
    path = PROJECT_ROOT
    os.chdir(path)
    # Move up one
    os.chdir('..')
    #Enter user folder
    #os.chdir('users/')
    #folder = os.getcwd()
    
    print(os.getcwd())

    os.chdir(os.getcwd()+'/MyBids/static/')

    folder = os.getcwd()



    try:
        #if User hasen't uploaded anything yet, create folder
        if " " in username:
            username = username.replace(" ","_")
            try:
                os.mkdir(folder+"/"+username + '/')
                os.chdir(folder+"/"+username+'/')
            except:
                os.chdir(folder+"/"+username+'/')
        else:
            try:
                os.mkdir(folder+"/"+username + '/')
                os.chdir(folder+"/"+username+'/')
            except:
                os.chdir(folder+"/"+username+'/')
    except:
        pass

    #change to user folder
    #os.chdir(username)


    folder = os.getcwd()

    try:
        os.mkdir(folder+"/images")
        os.chdir(folder+"/images")
    except:
        os.chdir(folder+"/images")



    folder = os.getcwd()



    #Fullpath to file
    fullpath = folder + "/" + imageFile.name

    print fullpath


    #Try to create file
    try:
        with open(fullpath, 'wb+') as destination:
            for chunk in imageFile.chunks():
                destination.write(chunk)


    except  ValidationError as e:

        print e.args

        return False

    fullpath = "/static/" + username+"/images/"+imageFile.name

    return fullpath
        
    