from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from book.forms import BookForm
from django.urls import reverse
from django.core.management import call_command
from book.models import Book
from django.core import serializers


def add_book(request):
    form = BookForm(request.POST, request.FILES)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "add_book.html", context)

def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
