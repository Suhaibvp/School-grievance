from django.db import models



class regadd(models.Model):
    uname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    cto=models.CharField(max_length=200)
    dep=models.CharField(max_length=200)
    cl=models.CharField(max_length=200)
    complaint=models.CharField(max_length=200)
    rply=models.CharField(max_length=200)
    cid=models.CharField(max_length=200)


class sadd(models.Model):
    sname=models.CharField(max_length=200)
    
    splace=models.CharField(max_length=200)
    scontact=models.CharField(max_length=200)
    
    semail=models.CharField(max_length=200)
    scource=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    img=models.CharField(max_length=200)


class principal(models.Model):
    prname=models.CharField(max_length=200)
    prplace=models.CharField(max_length=200)
    premail=models.CharField(max_length=200)
    prmob=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)


class hod(models.Model):
    hname=models.CharField(max_length=200)
    hplace=models.CharField(max_length=200)
    hemail=models.CharField(max_length=200)
    hmob=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    