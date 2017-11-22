from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^([^0-9]*)$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
    #first name validation
        if len(postData['fname']) <= 3:
            errors["fname"] = "First name should be more than 3 characters"
        if not NAME_REGEX.match(postData['fname']):
            errors['fname']="No numbers accepted in First Name!"
    #last name validation
        if len(postData['lname']) <= 2:
            errors["lname"] = "Last name should be more than 2 characters"
        if not NAME_REGEX.match(postData['lname']):
            errors['lname']="No numbers accepted in Last Name!"
    #email validation
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be empty"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Please enter a valid email address"
    #password validation
        if len(postData['password'])<8:
            errors["password"] = "Password should be more than 8 characters"
        if (postData['confirm_password'])!=(postData['password']):
            errors["confirm_password"] = "Password and Confirm password should match"
        
        hashed = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(5))
        return errors

    

    def login_validator(self, postData):
        query=User.objects.filter(email=postData['login_email'])
        print postData, "Bug"
        errors = {}
        if len(postData['login_email']) < 1:
            errors["login_email"] = "Please enter your email to login"
        if len(postData['login_password']) < 1:
            errors["login_email"] = "Please enter your password to login"
       
        if len(query)==0:
            errors['login_email'] = "User doesn't exist, please register"
        if len(errors) > 0:
            return errors


#password!login
        user=User.objects.filter(email=postData['login_email'])[0]
        if not bcrypt.checkpw(postData['login_password'].encode(), user.password.encode()):
            errors["login_password"] = "PWD invalid"
        return errors

            
        


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

class Wish(models.Model):
    item = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='wishes')
    created_by = models.CharField(max_length=255, default='none')
    created_at = models.DateTimeField(auto_now_add=True)