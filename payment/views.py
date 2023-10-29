from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import Account
from order.models import Order

@login_required
def payment(request):
    # Ambil profil pengguna yang sedang login
    user_profile = Account.objects.get(user=request.user)

    # Ambil pesanan yang sedang berlangsung oleh pengguna
    ongoing_orders = Order.objects.filter(user=request.user, is_completed=False)

    # Hitung total harga pesanan yang belum selesai
    total_price = sum(order.total_price() for order in ongoing_orders)

    if request.method == 'POST':
        # Proses pembayaran jika saldo mencukupi
        if user_profile.balance >= total_price:
            # Kurangi saldo pengguna
            user_profile.balance -= total_price
            user_profile.save()

            # Tandai pesanan-pesanan tersebut sebagai selesai
            ongoing_orders.update(is_completed=True)

            return render(request, 'payment/success.html')
        else:
            return render(request, 'payment/failure.html')

    return render(request, 'payment/payment.html', {'user_profile': user_profile, 'total_price': total_price})

