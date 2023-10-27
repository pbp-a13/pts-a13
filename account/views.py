from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Admin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def account_info(request):
    user = request.user 

    if Account.objects.filter(user=user).exists():
        # kalau bukan admin
        return render(request, 'member_account_info.html', user)

    if Admin.objects.filter(user=user).exists():
        # Kalau Admin
        return render(request, 'admin_account_info.html', user)

    # Kalau bukan keduanya
    return

def is_admin(user):
    return Admin.objects.filter(user=user).exists()

@user_passes_test(is_admin)
def all_member_page(request):
    # Retrieve all members from the database
    members = Account.objects.all()

    return render(request, 'admin_view_members.html', {'members': members})

def member_details(request, member_id):
    member = get_object_or_404(Account, id=member_id)

    return render(request, 'member_details.html', {'member': member})
