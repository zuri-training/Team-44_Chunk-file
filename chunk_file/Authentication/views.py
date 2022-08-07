from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout,authenticate
# from django.contrib.auth.decorators import login_required
from Authentication.forms import RegistrationForm,AccountAuthenticationForm

# Create your views here.
def signUp(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.email))

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('dashboard')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'Authentication/signUp.html', context)



def signIn(request, *args, **kwargs):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return redirect("dashboard")

	destination = get_redirect_if_exists(request)
	print("destination: " + str(destination))

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				if destination:
					return redirect(destination)
				return redirect("dashboard")

	else:
		form = AccountAuthenticationForm()

	context['login_form'] = form

	return render(request, "Authentication/login.html", context)


def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect



def signOut(request):
    logout(request)
    return redirect("index")

# =============================


def index(request):
    return render(request, "index.html")

# @login_required
def userDashboard(request):
    return render(request, "Dashboard.html",)


def aboutUs(request):
    return render(request, "aboutUs.html")


def contactUs(request):
    return render(request, "contactUs.html")


def FAQ(request):
    return render(request,"faq.html")

# @login_required
def settings(request):
    return render(request, "settings.html")

# @login_required
def splitPage(request):
    return render(request, "splitComplete.html")

# @login_required
def UploadPage(request):
    return render(request, "uploadingPage.html")

# @login_required
def storage(request):
    return render(request, "storagePage.html")
