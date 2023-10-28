from django.shortcuts import render, redirect
from account.models import Account

def top_up_balance(request):
    user = request.user
    user_balance, created = Account.saldo.objects.get_or_create(user=user, defaults={'balance': 0.00}) # ???

    if request.method == 'POST':
        # pengisian saldo
        amount = float(request.POST.get('amount', 0.00))
        user_balance.balance += amount
        user_balance.save()
        return redirect('account_info')  # Redirect ke halaman info akun setelah pengisian saldo

    return render(request, 'top_up_balance.html', {'user_balance': user_balance})
