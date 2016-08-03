from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

# Create your tests here.

class BidsTestCase(TestCase):
    
    def setUp(self):
        
        User.objects.create(
                            username = "xyz",
                            email = "xyz@ypk.com",
                            first_name = "xyz",
                            last_name = "ypk",
                            password = "1234"
                            )
        
        
    
    #Test user login
    def checkUserLogin(self):
        
        clnt = Client()
        
        data = dict(
                    email = "xyz@ypk.com",
                    password = "1234"
                    )
        
        
        response = clnt.post("http://127.0.0.1:8000/login", data)
        
        
        
        print(response.status_code)
        
        response.status_code
    
    #Test register of a user 
    def checkSinpuTest(self):
        
        #Checks csrf token 
        c = Client(enforce_csrf_checks = True)
        
        print (c.errors)
        
        clnt = Client()
        
        data = dict(
                    username = "xyz",
                    email = "xyz@ypk.com",
                    firstname = "xyz",
                    lastname = "xyzp",
                    password = "1234"
                    )
        
        response = clnt.post("http://127.0.0.1:8000/register", data)
        
        print(response.status_code)
        
        response.status_code
