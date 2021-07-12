from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm
from .models import *

class Loginform(ModelForm):
	class Meta:
		model = User
		fields = ['u_email','u_password','u_name']

class Registrationform(ModelForm):
	class Meta:
		model = User
		fields = ['u_name','u_email','u_mobile','u_password','u_city','u_pin']

class Forgotform(ModelForm):
	class Meta:
		model = User
		fields = ['u_email','u_password','u_password1']

class ComplaintForm(ModelForm):
	class Meta:
		model = Complaint
		fields = ['c_title', 'c_name','c_detail', 'c_photo1', 'c_photo2', 'c_state', 'c_city', 'c_fulladdress', 'c_area', 'c_pin', 'c_landmark', 'c_date']

class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ['cat_name']

class FeedbackForm(ModelForm):
	class Meta:
		model = Feedback
		fields = ['f_text','f_date','f_time']

class ProfileForm(ModelForm):
	class Meta:
		model = User
		fields = ['u_name','u_email','u_mobile','u_city','u_pin']

def login(request,template_name="login.html"):
	form = Loginform(request.POST or None)
	if (form.is_valid()):
		u_email = request.POST['u_email']
		u_password = request.POST['u_password']
		u_name = request.POST['u_name']
		b = User.objects.get(u_email=u_email, u_password=u_password,u_name=u_name)
		if (b):
			request.session['login_status'] = "1"
			request.session['loginname'] = b.u_email
			request.session['u_name'] = b.u_name
			return redirect("Management:home")
		else:
			return redirect("Management:login")
	return render(request, template_name)

def logout(request):
	#clear the session here...
	request.session['login_status'] = "0"
	return redirect("Management:login")


def home(request,template_name="home.html"):
	login_status = request.session['login_status']
	u_email = request.session['loginname']
	u_name = request.session['u_name']
	if(login_status=="1"):
		data = {"login_status":login_status,"u_email":u_email,"u_name":u_name }
		return render(request,template_name,data)
	else:
		return redirect("Management:login")


		
def register(request,template_name="register.html"):
	form = Registrationform(request.POST or None)
	if (form.is_valid()):
		form.save()
		return redirect("Management:login")
	return render(request, template_name, {"from":form})


def complaint(request,template_name="complaint.html"):
	login_status = request.session['login_status']
	u_name = request.session['loginname']
	if(login_status=="1"):
		form = ComplaintForm(request.POST or None)
		print(form)
		if (form.is_valid()):
			form.save()
			return redirect("Management:home")
		return render(request, template_name, {"form":form})
	else:
		return redirect("Management:login")


def forgot(request,template_name="forgot.html"):
	form = Forgotform(request.POST or None)
	if (form.is_valid()):
		u_email = request.POST['u_email']
		u_password = request.POST['u_password']
		u_password1 = request.POST['u_password1']
		b = User.objects.filter(u_email=u_email, u_password=u_password, u_password1=u_password)
		if (b):
			return redirect("Management:login")
		else:
			return redirect("Management:forgot")
	return render(request, template_name, {"form":form})


def category(request,template_name="category.html"):
	login_status = request.session['login_status']
	u_email = request.session['loginname']
	if(login_status=="1"):
		form = CategoryForm(request.POST or None)
		if (form.is_valid()):
			form.save()
			return redirect("Management:complaint")	
		return render(request, template_name,{"form":form})
	else:
		return redirect("Management:login")


def feedback(request,template_name="feedback.html"):
	login_status = request.session['login_status']
	u_email = request.session['loginname']
	if(login_status=="1"):
		form = FeedbackForm(request.POST or None)
		if (form.is_valid()):
			form.save()
			return redirect("Management:home")
		return render(request, template_name, {"form":form})
	else:
		return redirect("Management:login")


'''def edit_profile(request,template_name="edit_profile.html"):
	login_status = request.session['login_status']
	u_email = request.session['loginname']
	u_name = request.session['u_name']
	if(login_status=="1"):	
		b = get_object_or_404(User)			
		form = ProfileForm(request.POST or None, instance=b)
		if form.is_valid():
			form.save()  
			return redirect('Management:home')
		return render(request, template_name,data)		
	else:
		return redirect("Management:login")'''


