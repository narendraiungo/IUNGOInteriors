from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from LIstings.forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.apps import apps
from .models import IungoUser
from django.contrib import messages
from django.views.generic import ListView,CreateView,UpdateView
# Create your views here.

def usercreation(request):
    if request.method == 'POST':
        #import pdb;pdb.set_trace()
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            request.session['user'] = username
            return redirect('userauthentication')

    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def userauthentication(request):
    if request.session.has_key('user'):
        username = request.session['user']
        user = IungoUser.objects.get(username=username)
        return render(request, 'userpage.html')
    return redirect('userpage')

def userpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user'] = username
                return redirect('userauthentication')
            messages.add_message(request, messages.INFO, 'User is Not Active.')
            return redirect('userpage')
        messages.add_message(request, messages.INFO, 'Please Check Your Login Credentials.')
        return redirect('userpage')

    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})



def load_categories(request):
    client_type = request.GET.get('client_type')
    model = apps.get_model('LIstings', client_type)
    client_category = model.objects.all()
    return render(request, 'registration/Category_dropdown.html', {'categories': client_category})

def user_list(request, user_type):
    users = IungoUser.objects.filter(client_category=user_type)
    return render(request, 'user_list.html',{'users':users})

