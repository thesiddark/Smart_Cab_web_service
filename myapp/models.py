from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    photo = models.CharField(max_length=400)
    dob = models.DateField()
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100,default="pending")
    pin = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Driver(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    photo=models.CharField(max_length=400)
    proof=models.CharField(max_length=400)
    vphoto=models.CharField(max_length=400)
    dob=models.DateField()
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    vnumber=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Ambulance_Driver(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    photo=models.CharField(max_length=400)
    proof=models.CharField(max_length=400)
    vphoto=models.CharField(max_length=400,default="no")
    dob=models.DateField()
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    vreg_no=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    status=models.CharField(max_length=100,default="pending")
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)



class Feedback(models.Model):
    date = models.DateField()
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    Feed_back=models.CharField(max_length=100)


class Complaint(models.Model):
    date = models.DateField()
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=1000)
    status=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)

class Driver_Request(models.Model):
    date=models.DateField()
    source=models.CharField(max_length=500)
    destination=models.CharField(max_length=500)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    DRIVER=models.ForeignKey(Driver,on_delete=models.CASCADE)
    status=models.CharField(max_length=100)

class Ambulance_request(models.Model):
    date = models.DateField()
    source = models.CharField(max_length=500)
    destination = models.CharField(max_length=500)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    AMBULANCE_DRIVER = models.ForeignKey(Ambulance_Driver,on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

class Payment_to_cab(models.Model):
    amount=models.FloatField()
    date = models.DateField()
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    REQUEST=models.ForeignKey(Driver_Request,on_delete=models.CASCADE)
    status = models.CharField(max_length=100)



class Payment_to_ambulance(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    REQUEST = models.ForeignKey(Ambulance_request, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)


class Location(models.Model):
    latitude=models.CharField(max_length=50)
    longitude=models.CharField(max_length=50)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)







