import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from main.models import Admin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from .forms import UserForm, AccountForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import main.views
from django.views.decorators.csrf import csrf_exempt

def register(request):
    user_form = UserCreationForm()
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        #account_form = AccountForm(request.POST)
        if user_form.is_valid(): #and account_form.is_valid():
            new_user = user_form.save()
            #account_form.save()
            messages.success(request, ('Your profile was successfully created!'))
            return redirect('main:show_main')
        else:
            messages.error(request, ('Please correct the error below.'))
        #account_form = AccountForm()
    context = {
        'user_form': user_form,
        #'account_form': account_form,
    }
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

    if Admin.objects.filter(account=user).exists():
        admin = Admin.objects.get(account=user)
        # If the user is an admin
        if admin.is_admin_mode:
            # If the user is currently in admin mode
            return render(request, 'admin_account_info.html', {'admin': admin})
        else:
            # If the user is an admin but currently in account mode
            return render(request, 'member_account_info.html', {'account': admin})

    elif Account.objects.filter(user=user).exists():
        # If the user is not an admin but has an account
        account = Account.objects.get(user=user)
        return render(request, 'member_account_info.html', {'account': account})

    # If the user is not logged in or does not have an account
    return redirect('login')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:show_main'))

### so far ini belum kepake.. gw jg udh ganti modelsnya jd mungkin hrs dimodif dikit
def is_admin(user):
    return Admin.objects.filter(user=user).exists()

@user_passes_test(is_admin)
def all_member_page(request):
    # Retrieve all members from the database
    accounts = Account.objects.all().order_by('user__username')

    return render(request, 'all_member_page.html', {'account': accounts})

def member_details(request, member_id):
    account = get_object_or_404(Account, id=member_id)

    return render(request, 'member_detail.html', {'account': account})


def get_account_info(request):
    user = request.user 

    if Admin.objects.filter(account=user).exists():
        admin = Admin.objects.get(account=user)
        # If the user is an admin
        if admin.is_admin_mode:
            # If the user is currently in admin mode
            return JsonResponse({'nama': admin.nama, 'email': admin.email, 'alamat': admin.alamat})
        else:
            # If the user is an admin but currently in account mode
            return JsonResponse({'nama': admin.nama, 'email': admin.email, 'alamat': admin.alamat})

    elif Account.objects.filter(user=user).exists():
        # If the user is not an admin but has an account
        account = Account.objects.get(user=user)
        return JsonResponse({'nama': account.nama, 'email': account.email, 'alamat': account.alamat})

    # If the user is not logged in or does not have an account
    return JsonResponse({'error': 'Not logged in'}, status=401)

@csrf_exempt
def update_account_info(request):
    if request.method == 'POST':
        user = request.user 
        data = json.loads(request.body)

        if Admin.objects.filter(account=user).exists():
            admin = Admin.objects.get(account=user)
            # If the user is an admin
            if admin.is_admin_mode:
                # If the user is currently in admin mode
                admin.nama = data['nama']
                admin.email = data['email']
                admin.alamat = data['alamat']
                admin.save()
                return JsonResponse({'status': 'success'})
            else:
                # If the user is an admin but currently in account mode
                admin.nama = data['nama']
                admin.email = data['email']
                admin.alamat = data['alamat']
                admin.save()
                return JsonResponse({'status': 'success'})

        elif Account.objects.filter(user=user).exists():
            # If the user is not an admin but has an account
            account = Account.objects.get(user=user)
            account.nama = data['nama']
            account.email = data['email']
            account.alamat = data['alamat']
            account.save()
            return JsonResponse({'status': 'success'})

    # If the user is not logged in or does not have an account or it's not a POST request
    return JsonResponse({'error': 'Not logged in or invalid request'}, status=401)


def search_members(request):
    query = request.GET.get('query', '')
    
    # Perform the member search in your database using the username field
    results = Account.objects.filter(user__username__icontains=query)

    # Prepare the results in JSON format
    members = [{'id': member.id, 'username': member.user.username, 'nama': member.nama} for member in results]

    return JsonResponse(members, safe=False)