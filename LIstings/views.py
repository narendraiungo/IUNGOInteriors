from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.apps import apps
from .models import IungoUser, Architects, InteriorDesigners, Architects_interiordesigenrs, Contractors
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q
from bookappointment.models import sub_category,Category,Client

# Create your views here.


def home(request):
    architects = Architects.objects.all()
    interiordesigners = InteriorDesigners.objects.all()
    architects_interiors = Architects_interiordesigenrs.objects.all()
    contractors = Contractors.objects.all()
    return render(request, 'index.html', {'architects': architects, 'interiordesigners': interiordesigners,
                                          'architects_interiors': architects_interiors, 'contractors': contractors})


def usercreation(request):
    if request.method == 'POST':
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
    return render(request, 'user_list.html', {'users': users})


def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(content__icontains=query)

            results= sub_category.objects.filter(lookups).distinct()
            result1=Category.objects.filter(lookups).distinct()
            context={'results': results,'result':result1,
                     'submitbutton': submitbutton}

            return render(request, 'searching.html', context)

        else:
            return render(request, 'searching.html')

    else:
        return render(request, 'searching.html')