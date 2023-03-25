from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
GENDER_CHOICES = [('M', 'Male'),('F', 'Female'),('O', 'Other'),]
MEAL_CHOICE=[('B', 'Breakfast'),('L', 'Lunch'),('D', 'Dinner'),]
PMT_CHOICE=[('C','Card'), ('U','UPI')]
PKG_CAT=[('A','Adventure'),('B','Beach'),('R','Religious'),('H','Heritage'),]

class Address(models.Model):
    id=models.AutoField(primary_key=True)  
    add_no=models.CharField(max_length=5)
    add_street=models.CharField(max_length=50)
    add_city=models.CharField(max_length=15)
    add_state=models.CharField(max_length=15)
    add_country=models.CharField(max_length=25)
    add_zip=models.CharField(max_length=6)
    
    def __str__(self):
        return f"{self.add_no}, {self.add_street}, {self.add_city},{self.add_country},{self.add_zip}"


class Admin(models.Model):
    id=models.AutoField(primary_key=True)  
    admin_name=models.CharField(max_length=50)
    admin_gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    admin_add=models.ForeignKey(Address,on_delete=models.CASCADE)
    admin_cno=models.CharField(max_length=10)
    admin_email=models.EmailField(null=True)
    admin_dob=models.DateField(null=True)
    admin_pswd=models.CharField(max_length=8)

    def __str__(self):
        return self.admin_name
    
class Customer(models.Model):
        id=models.AutoField(primary_key=True)
        customer_name=models.CharField(max_length=50,default=0)      
        customer_gender=models.CharField(max_length=6,choices=GENDER_CHOICES)
        customer_add=models.ForeignKey(Address,on_delete=models.CASCADE)
        customer_cno=models.CharField(max_length=10)
        customer_dob=models.DateField(null=True)
        customer_email=models.EmailField(unique=True)
        customer_pswd=models.CharField(max_length=8)
        #customer_img = models.ImageField(upload_to='woman.png')
        
        def __str__(self):
            return self.customer_name
        
class Agent(models.Model):
        id=models.AutoField(primary_key=True)
        agency_name=models.CharField(max_length=20)       
        agent_name=models.CharField(max_length=50,default=0)
        agent_gender=models.CharField(max_length=7,choices=GENDER_CHOICES)
        agent_add=models.ForeignKey(Address,on_delete=models.CASCADE,default=0)
        agent_cno=models.CharField(max_length=10)
        agent_dob=models.DateField()
        agent_email=models.EmailField(unique=True)
        agent_pswd=models.CharField(max_length=8)
        
        def __str__(self):
            return self.agent_name
    
class Packages(models.Model):
    id=models.AutoField(primary_key=True)
    pkg_type=models.CharField(max_length=30)
    pkg_title=models.CharField(max_length=30)
    dep_date=models.DateField()
    pkg_from=models.CharField(max_length=20)
    pkg_to=models.CharField(max_length=20)
    #pkg_pic=models.ImageField()
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE,default=0)
    pkg_dec=models.TextField(max_length=255)
    pkg_price=models.IntegerField()
    pkg_days=models.IntegerField()
    pkg_night=models.IntegerField()
    tota_seats=models.IntegerField()
    avil_seats=models.IntegerField()
    pkg_type=models.CharField(max_length=10,choices=PKG_CAT)
    pkg_status=models.BooleanField(default=True)
    pkg_img=models.ImageField(upload_to='destination-2.jpg',default=1)
    @property
    def status(self):
        if self.is_booked:
            return "booked"
        else:
            return "cancelled"
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.pkg_title
    

class Hotel(models.Model):
    id=models.AutoField(primary_key=True)
    hotel_name=models.CharField(max_length=20)
    hotel_add=models.ForeignKey(Address,on_delete=models.CASCADE,default=0)
    hotel_type=models.CharField(max_length=20)
    meal_type=models.CharField(max_length=20,choices=MEAL_CHOICE)

class Booking(models.Model):
    id=models.AutoField(primary_key=True)
    package=models.ForeignKey(Packages,on_delete=models.CASCADE)
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    bkg_date=models.DateField()
    number_of_person=models.IntegerField()
    price=models.CharField(max_length=6)
    seat=models.CharField(max_length=5,default=0)

class Payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE,default=0)
    payment_time=models.TimeField()
    payment_method=models.CharField(max_length=10,choices=PMT_CHOICE)
    payment_amt=models.IntegerField()

class Cancellation(models.Model):
    id=models.AutoField(primary_key=True)
    booking=models.ForeignKey(Booking,on_delete=models.CASCADE)
    cl_time=models.TimeField()
    cl_reason=models.CharField(max_length=255)
    refund_st=models.BooleanField(default=False)

class Enquiry(models.Model):
    id=models.AutoField(primary_key=True)
    eqry_name=models.CharField(max_length=20)
    eqry_email=models.EmailField(unique=True)
    eqry_remark=models.CharField(max_length=100)
    eqry_type=models.CharField(max_length=10)
    eqry_date=models.DateField()

class Feedback(models.Model):
    id=models.AutoField(primary_key=True)
    fb=models.CharField(max_length=255)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

# class User(AbstractUser):
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField(unique=True, null=True)
#     bio = models.TextField(null=True)

#     avatar = models.ImageField(null=True, default="avatar.png")

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
