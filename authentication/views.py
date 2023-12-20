from django.contrib.auth import logout as auth_logout
import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account.models import Account
from main.models import Admin
from django.contrib.auth import get_user


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            response = {
                "username": user.username,
                "status": True,
                "message": "Login sukses!",
                "is_admin": True,
                "is_admin_mode": False,
            }
            try:
                response["is_admin_mode"] = request.user.account.admin.is_admin_mode
            except:
                response["is_admin"] = False
            print(response)
            # Status login sukses.
            return JsonResponse(
                response, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)


...


@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout gagal."
        }, status=401)


@csrf_exempt
def get_account(request):
    user = get_user(request)
    # print(user)
    if user is not None:
        if user.is_active:
            if Admin.objects.filter(account=user).exists():
                admin = Admin.objects.get(account=user)
                account = Account.objects.get(user=user)
                if admin.is_admin_mode:
                    return JsonResponse({'nama': admin.nama, 'email': admin.email, 'alamat': admin.alamat, "username": admin.user.username, "orders_completed": admin.orders_completed}, status=200)
                else:
                    return JsonResponse({'nama': admin.nama, 'email': admin.email, 'alamat': admin.alamat, "username": admin.user.username, "saldo": account.saldo}, status=200)
            elif Account.objects.filter(user=user).exists():
                account = Account.objects.get(user=user)
                return JsonResponse({'nama': account.nama, 'email': account.email, 'alamat': account.alamat, "username": account.user.username, "saldo": account.saldo}, status=200)
            else:
                return JsonResponse({'error': 'Not logged in'}, status=401)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)


@csrf_exempt
def update_account(request):
    user = get_user(request)
    print(user)
    if user is not None:
        if user.is_active:
            data = json.loads(request.body)
            if Admin.objects.filter(account=user).exists():
                admin = Admin.objects.get(account=user)
                account = Account.objects.get(user=user)
                if admin.is_admin_mode:
                    admin.nama = data['nama']
                    admin.email = data['email']
                    admin.alamat = data['alamat']
                    admin.save()
                    return JsonResponse({'status': 'success', 'nama': admin.nama, 'email': admin.email, 'alamat': admin.alamat})
                else:
                    admin.nama = data['nama']
                    admin.email = data['email']
                    admin.alamat = data['alamat']
                    admin.save()
                    return JsonResponse({'status': 'success', 'nama': admin.nama, 'email': admin.email, 'alamat': admin.alamat})
            elif Account.objects.filter(user=user).exists():
                account = Account.objects.get(user=user)
                account.nama = data['nama']
                account.email = data['email']
                account.alamat = data['alamat']
                account.save()
                return JsonResponse({'status': 'success', 'nama': account.nama, 'email': account.email, 'alamat': account.alamat})
            else:
                return JsonResponse({'error': 'Not logged in'}, status=401)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)


@csrf_exempt
def get_all_members(request):
    # Retrieve all members from the database
    accounts = Account.objects.all().order_by('user__username')

    # Convert queryset to a list of dictionaries
    members_data = [
        {'username': account.user.username, 'nama': account.nama, 'saldo': account.saldo,
            'alamat': account.alamat, 'email': account.email,
            'user': {
                'username': account.user.username,
                'email': account.user.email,
                'first_name': account.user.first_name,
                'last_name': account.user.last_name,
            }}
        for account in accounts
    ]
    print(members_data)

    return JsonResponse({'members': members_data}, status=200)
