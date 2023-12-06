from django.shortcuts import render
from django.http import HttpResponseRedirect
from book.forms import BookForm
from django.urls import reverse
from django.core.management import call_command


def add_book(request):
    form = BookForm(request.POST, request.FILES)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "add_book.html", context)

from django.core.management import call_command


def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "books")
