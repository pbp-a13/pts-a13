from django.shortcuts import render, redirect
from account.models import Account

def top_up_balance(request):
    user = request.user
    user_account, created = Account.objects.get_or_create(user=user, defaults={'saldo': 0})

    if request.method == 'POST':
        amount = int(request.POST.get('amount', 0))
        user_account.saldo += amount
        user_account.save()
        return redirect('account_info')  # Redirect ke halaman info akun setelah pengisian saldo

    return render(request, 'top_up_balance.html', {'user_account': user_account})
