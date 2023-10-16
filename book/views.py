from django.shortcuts import render
from django.http import HttpResponseRedirect
from book.forms import BookForm
from django.urls import reverse


def add_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "add_book.html", context)
