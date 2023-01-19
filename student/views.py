from django.http import HttpResponse
from django.shortcuts import render
# from .models import testtb
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .model import *


















# def sfview(request):
#     sv=sadd.objects.all()
#     return render(request,'sfview.html',{'result':sv})

# def ufview(request):
#     uv=regadd.objects.all()
#     return render(request,'ufview.html',{'result':uv})



# def prview(request):
#     return render(request,'prview.html')

# def prinadd(request):
#     return render(request,'prinadd.html')







    







        

# def vprofile(request):
#     sc=request.session['uid']
#     sd=regadd.objects.get(id=sc)
#     return render(request,'prview.html',{'result':sd})


# def sdelete(request,id):
#     mark=sadd.objects.get(pk=id)
#     mark.delete()
#     return redirect(sfview)


# def supdate(request,id):
#     mark=sadd.objects.get(pk=id)
#     return render(request,'supdate.html',{'res':mark})


# def ssupdate(request,id):
#     if request.method=='POST':
#         sname=request.POST.get('sname')
#         sage=request.POST.get('sage')
#         splace=request.POST.get('splace')
#         scontact=request.POST.get('scontact')
#         pcontact=request.POST.get('pcontact')
#         semail=request.POST.get('semail')
#         scource=request.POST.get('scource')
#         img=request.FILES['img']
#         a=FileSystemStorage()
#         b=a.save(img.name,img)
#         log=sadd(sname=sname,sage=sage,splace=splace,scontact=scontact,pcontact=pcontact,semail=semail,scource=scource,id=id,img=img)
#         log.save()
#         return redirect(sfview)



# def uupdate(request,id):
#     mark=regadd.objects.get(pk=id)
#     return render(request,'uupdate.html',{'res':mark})


# def uuupdate(request,id):
#     if request.method=='POST':
#         uname=request.POST.get('uname')
#         uage=request.POST.get('uage')
#         uplace=request.POST.get('uplace')
#         ucontact=request.POST.get('ucontact')
#         email=request.POST.get('email')
#         usubject=request.POST.get('usubject')
#         uqualification=request.POST.get('uqualification')
#         uexperience=request.POST.get('uexperience')
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         img=request.FILES['img']
#         a=FileSystemStorage()
#         b=a.save(img.name,img)
#         log=regadd(uname=uname,uage=uage,uplace=uplace,ucontact=ucontact,email=email,usubject=usubject,uqualification=uqualification,uexperience=uexperience,username=username,password=password,id=id,img=img)
#         log.save()
#         return redirect(ufview)


# def udelete(request,id):
#     mark=regadd.objects.get(pk=id)
#     mark.delete()
#     return redirect(ufview)














        


#START

def home(request):
    return render(request,'index.html')


def studadd(request):
    
    if request.method=='POST':
        sname=request.POST.get('sname')
        username=request.POST.get('username')
        splace=request.POST.get('splace')
        scontact=request.POST.get('scontact')
        password=request.POST.get('password')
        semail=request.POST.get('semail')
        scource=request.POST.get('scource')
        img=request.FILES['img']
        a=FileSystemStorage()
        b=a.save(img.name,img)
        log=sadd(sname=sname,username=username,splace=splace,scontact=scontact,password=password,semail=semail,scource=scource,img=img)
        log.save()
    return render(request,'register.html')


def sstudent(request):
    sc=sadd.objects.all()
    return render(request,'sstudent.html',{'result':sc})




def ulogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    print(password)
    if username == 'admin123' and password =='admin':
        request.session['logins'] = username
        request.session['admin'] ='admin'
        return render(request,'index.html')

    elif sadd.objects.filter(username=username,password=password).exists():
        users=sadd.objects.get(username=request.POST['username'],password=password)
        if users.password == request.POST['password']:
            request.session['sid'] = users.id
            request.session['sname'] = users.sname
            request.session['username'] = username
            request.session['asha'] = 'asha'
            return render(request,'index.html')

    elif principal.objects.filter(username=username,password=password).exists():
        users=principal.objects.get(username=request.POST['username'],password=password)
        if users.password == request.POST['password']:
            request.session['pid'] = users.id
            request.session['prname'] = users.prname

            request.session['username'] = username

            request.session['user'] = 'user'

            
            return render(request,'index.html')


    elif hod.objects.filter(username=username,password=password).exists():
        users=hod.objects.get(username=request.POST['username'],password=password)
        if users.password == request.POST['password']:
            request.session['hid'] = users.id
            request.session['hname'] = users.hname

            request.session['email'] = username

            request.session['user'] = 'user'

            
            return render(request,'index.html')


    else:
            return render(request, 'login.html', {'status': 'failed'})


def ulogout(request):
    request.session.delete()
    return redirect('/')



def prinsadd(request):
    if request.method=='POST':
        prname=request.POST.get('prname')
        prplace=request.POST.get('prplace')
        premail=request.POST.get('premail')
        prmob=request.POST.get('prmob')
        username=request.POST.get('username')
        password=request.POST.get('password')
        log=principal(prname=prname,prplace=prplace,premail=premail,prmob=prmob,username=username,password=password)
        log.save()
    return render(request,'prinadd.html')



def sprince(request):
    sv=principal.objects.all()
    return render(request,'sprince.html',{'result':sv})



def hoadd(request):
    if request.method=='POST':
        hname=request.POST.get('hname')
        hplace=request.POST.get('hplace')
        hemail=request.POST.get('hemail')
        hmob=request.POST.get('hmob')
        username=request.POST.get('username')
        password=request.POST.get('password')
        log=hod(hname=hname,hplace=hplace,hemail=hemail,hmob=hmob,username=username,password=password)
        log.save()
    return render(request,'hadd.html')



def shod(request):
    sc=hod.objects.all()
    return render(request,'shod.html',{'result':sc})



def creg(request):
    c=request.session['sname']
    if request.method=='POST':
        uname=request.POST.get('uname')

        email=request.POST.get('email')
        cto=request.POST.get('cto')
        dep=request.POST.get('dep')
        cl=request.POST.get('cl')
        complaint=request.POST.get('complaint')
        rply='Pending'

        log=regadd(uname=uname,email=email,cto=cto,dep=dep,cl=cl,complaint=complaint,rply=rply,cid=c)
        log.save()
    return render(request,'studadd.html')


def cshow(request):
    sc=regadd.objects.all()
    return render(request,'complaints.html',{'result':sc})


def csshow(request):
    b=request.session['sname']
    sc=regadd.objects.filter(cid=b)
    return render(request,'cstudent.html',{'result':sc})


def cdelete(request,id):
    mark=regadd.objects.get(pk=id)
    mark.delete()
    return redirect(csshow)



def cpshow(request):
    sc=regadd.objects.filter(cto='Principal')
    return render(request,'cprince.html',{'result':sc})

def chshow(request):
    sc=regadd.objects.filter(cto='hod')
    return render(request,'chod.html',{'result':sc})





# def ssupdate(request,id):
#     if request.method=='POST':
#         sname=request.POST.get('sname')
#         sage=request.POST.get('sage')
#         splace=request.POST.get('splace')
#         scontact=request.POST.get('scontact')
#         pcontact=request.POST.get('pcontact')
#         semail=request.POST.get('semail')
#         scource=request.POST.get('scource')
#         img=request.FILES['img']
#         a=FileSystemStorage()
#         b=a.save(img.name,img)
#         log=sadd(sname=sname,sage=sage,splace=splace,scontact=scontact,pcontact=pcontact,semail=semail,scource=scource,id=id,img=img)
#         log.save()
#         return redirect(sfview)





# def rp(request,id):
#     if request.method=='POST':
#         uname=request.POST.get('uname')

#         email=request.POST.get('email')
#         cto=request.POST.get('cto')
#         dep=request.POST.get('dep')
#         cl=request.POST.get('cl')
#         complaint=request.POST.get('complaint')

#         log=regadd(uname=uname,email=email,cto=cto,dep=dep,cl=cl,complaint=complaint,id=id)
#         log.save()
#         return redirect(cpshow)

def studup(request,id):
    mark=sadd.objects.get(pk=id)
    return render(request,'sstudent.html',{'result':mark})

def sstudup(request,id):
    if request.method=='POST':
        sname=request.POST.get('sname')
        username=request.POST.get('username')
        splace=request.POST.get('splace')
        scontact=request.POST.get('scontact')
        password=request.POST.get('password')
        semail=request.POST.get('semail')
        scource=request.POST.get('scource')
        img=request.FILES['img']
        a=FileSystemStorage()
        b=a.save(img.name,img)
        log=sadd(sname=sname,username=username,splace=splace,scontact=scontact,password=password,semail=semail,scource=scource,img=img,id=id)
        log.save()
        return redirect()




def rp(request,id):
    mark=regadd.objects.get(pk=id)
    return render(request,'pc.html',{'result':mark})

def rrp(request,id):
    if request.method=='POST':
        cid=request.POST.get('cid')
        uname=request.POST.get('uname')

        email=request.POST.get('email')
        cto=request.POST.get('cto')
        dep=request.POST.get('dep')
        cl=request.POST.get('cl')
        complaint=request.POST.get('complaint')
        rply=request.POST.get('rply')

        log=regadd(uname=uname,email=email,cto=cto,dep=dep,cl=cl,complaint=complaint,id=id,rply=rply,cid=cid)
        log.save()
        return redirect(cpshow)

def rh(request,id):
    mark=regadd.objects.get(pk=id)
    return render(request,'hc.html',{'result':mark})

def rrh(request,id):
    if request.method=='POST':
        uname=request.POST.get('uname')

        email=request.POST.get('email')
        cto=request.POST.get('cto')
        dep=request.POST.get('dep')
        cl=request.POST.get('cl')
        complaint=request.POST.get('complaint')
        rply=request.POST.get('rply')

        log=regadd(uname=uname,email=email,cto=cto,dep=dep,cl=cl,complaint=complaint,id=id,rply=rply)
        log.save()
        return redirect(chshow)
    


def pprofile(request):
    return render(request,'pprofile.html')


def pprofile(request):
    se=request.session['pid']
    sv=principal.objects.get(id=se)
    return render(request,'pprofile.html',{'result':sv})


def hprofile(request):
    se=request.session['hid']
    sc=hod.objects.get(id=se)
    return render(request,'hprofile.html',{'result':sc})


def sprofile(request):
    se=request.session['sid']
    sc=sadd.objects.get(id=se)
    return render(request,'sprofile.html',{'result':sc})