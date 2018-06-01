from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import hashlib
from .models import Citizen
# import django.template.loader
# Create your views here.

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def index(request):
	action_path = "dashboard/"
	template = loader.get_template('portal/index.html')
	return HttpResponse(template.render({"action_path":action_path},request) )

def dashboard(request):
	template = loader.get_template('portal/index.html')
	
	action_path = ""
	if (request.POST['aadhar']=='') or (request.POST['password']==''):
		return HttpResponse(template.render({'error':"Partially filled form","action_path":action_path},request))

	try:
		selected_row = Citizen.objects.get(aadhar_number = request.POST['aadhar'])
	except (KeyError, Citizen.DoesNotExist):
		return HttpResponse(template.render({'error':"Incorrect Aadhar or Password","action_path":action_path},request))
	else:
		# if check_password(selected_row.password , request.POST['password']):
		if (selected_row.password == request.POST['password']):
			teplate2 = loader.get_template('portal/dashboard.html')
			return HttpResponse(teplate2.render({'points':selected_row.points},request))
		else:
			return HttpResponse(template.render({'error':"Incorrect Aadhar or Password","action_path":action_path},request))