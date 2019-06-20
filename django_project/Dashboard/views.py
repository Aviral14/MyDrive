from django.shortcuts import render,redirect
from django import forms
from . import models
from django.contrib import messages
from . import forms as forms_local


def dashboard(request):
	user=request.user
	return render(request,'Dashboard/dashboard.html',{'user':user})

def view(request):
    user=request.user
    datalist=user.filedata_set.all()
    return render(request,'Dashboard/view.html',{'datalist':datalist})

def upload(request):
	if request.method == 'POST':
		form = forms_local.DocumentForm(request.POST,request.FILES)
		if form.is_valid():
			form_obj=form.save(commit=False)
			form_obj.user=request.user
			form_obj.save()
			messages.success(request,'File Successfully Uploaded')
			return redirect('http://localhost:8000/dashboard/')
	else:
		form = forms_local.DocumentForm()
	return render(request, 'Dashboard/upload.html', {'form': form})	
