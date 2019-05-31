from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
	'''REGISTER USER'''
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account created')
			#return redirect('home')
			cxt = {'var':username}
			return render(request, 'home.html',cxt)
	else:
		form = UserRegisterForm()
	#form = UserCreationForm()
	return render(request, 'register.html',{'form':form})

