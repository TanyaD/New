from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *

def index(request): 
    return render(request, 'Loginandregistration/index.html')

def success(request): 

    try:
        request.session['id']
    except KeyError:
        messages.warning(request, "You must be logged in to see the books")
        return redirect('/')
    
    mywish= User.objects.get(id=request.session['id']).wishes.all()
    users = User.objects.all()
    allwishes=Wish.objects.all()

    loginuser=User.objects.get(id=request.session['id'])
    others=[]
    for other_user in users:
        if other_user.id !=loginuser:
            others.append(other_user)

    mywishes=loginuser.wishes.all()


    otherwishes=[]
    for other_wish in allwishes:
        if other_wish not in mywishes:
            otherwishes.append(other_wish)

    #otherwishes = User.objects.exclude(id__in=User.objects.get(id=request.session['id'])).wishes.all()

    context = {
        'allusers': User.objects.all(),
        'user': User.objects.get(id=request.session['id']),
        'wishes': Wish.objects.all(),
        'mywish': mywish,
        'otherwishes': otherwishes
    }
    print context
    return render(request, 'Loginandregistration/success.html', context)




def login(request):

    errors = User.objects.login_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error,extra_tags=tag)
        return redirect('/')

    request.session['id']=User.objects.get(email=request.POST['login_email']).id
    print request.session['id']
    return redirect('/success')

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def show(request,id):
    try:
        request.session['id']
    except KeyError:
        messages.warning(request, "You must be logged in to see the books")
        return redirect('/')
    
    context = {
        'item': Wish.objects.get(id=id),
        'users': Wish.objects.get(id=id).users.all()
    }
    
    return render(request, 'Loginandregistration/wish.html', context)

def createw(request):
    return render(request,'Loginandregistration/create.html' )

def add(request):
    #inst=Wish.objects.create(item=request.POST['itemname'], created_by=request.session['id'])
    inst=User.objects.get(id=request.session['id']).wishes.create(item=request.POST['itemname'], created_by=User.objects.get(id=request.session['id']).first_name)
    return redirect('/success')

def remove(request, id):
    a=Wish.objects.get(id=id)
    b=User.objects.get(id=request.session['id'])
    b.wishes.remove(a)
    return redirect('/success')

def create(request):
    errors=User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error,extra_tags=tag)
        return redirect('/')
    
    hashed = bcrypt.hashpw((request.POST['password'].encode()), bcrypt.gensalt(5))
    query=User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'], email=request.POST['email'], password=hashed)
    request.session['id']=query.id

    return redirect('/success')

def addfrom(request,id):
    a=Wish.objects.get(id=id)
    b=User.objects.get(id=request.session['id'])
    b.wishes.add(a)
    return redirect('/success')


    


