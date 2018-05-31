from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import hashlib
from .models import MainModel
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
	template = loader.get_template('portal/index.html')
	return HttpResponse(template.render({},request) )

def dashboard(request):
	template = loader.get_template('portal/index.html')
	if (request.post['aadhar']=='') or (request.post['password']==''):
		return HttpResponse(template.render({'error':"Partially filled form"},request))

	try:
		selected_row = MainModel.objects.get(aadhar_number = request.post['aadhar'])
	except (KeyError, MainModel.DoesNotExist):
		return HttpResponse(template.render({'error':"Incorrect Aadhar or Password"},request))
	else:
		if check_password(selected_row.password , request.post['password']):
			teplate2 = loader.get_template('portal/dashboard.html')
			return HttpResponse(teplate2.render({'points':""},request))
		else:
			return HttpResponse(template.render({'error':"Incorrect Aadhar or Password"},request))