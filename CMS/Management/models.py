 from django.db import models

# Create your models here.
#Model of manager:
class Manager(models.Model):
	m_id = models.CharField(max_length=5)
	m_name = models.CharField(max_length=30)
	m_mobile = models.IntegerField(default=0)
	m_password = models.CharField(max_length=30)
	m_email = models.CharField(max_length=30)	
	def __str__(self):
		return self.m_name

#Model of user:
class User(models.Model):
	u_id = models.CharField(max_length=5)
	u_name = models.CharField(max_length=30)
	u_email = models.CharField(max_length=30)
	u_mobile = models.IntegerField(default=0)
	u_password = models.CharField(max_length=30)
	u_password1 = models.CharField(max_length=30)
	u_city = models.CharField(max_length=30)
	u_pin = models.IntegerField(default=0)
	def __str__(self):
		return self.u_email,self.u_password


#Model for Category:
class Category(models.Model):
	cat_id = models.CharField(max_length=30)
	cat_name = models.CharField(max_length=30)
	def __str__(self):
		return self.cat_name

#Model of Complaint :
class Complaint(models.Model):
	c_id = models.CharField(max_length=5)
	c_title = models.CharField(max_length=30)
	c_name = models.CharField(max_length=30)	
	c_detail = models.CharField(max_length=1000)
	c_photo1 = models.ImageField(upload_to='images/')
	c_photo2 = models.ImageField(upload_to='images/')
	c_state = models.CharField(max_length=30)
	c_city = models.CharField(max_length=30)
	c_fulladdress = models.CharField(max_length=100)
	c_area = models.CharField(max_length=30)
	c_pin = models.IntegerField(default=0)
	c_landmark = models.CharField(max_length=30)
	c_date = models.CharField(max_length=10)
	c_status = models.CharField(max_length=30)
	def __str__(self):
		return self.c_title

#Models of Feedback:
class Feedback(models.Model):
	f_id = models.CharField(max_length=5)
	f_text = models.CharField(max_length=1000)
	f_date = models.CharField(max_length=10)
	f_time = models.CharField(max_length=10)
	def __str__(self):
		return self.f_text