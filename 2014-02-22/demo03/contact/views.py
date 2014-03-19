from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from contact.forms import ContactForm

# Create your views here.

def contact_page(request):
    form = ContactForm()
    completed = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            completed = True
    context = {'form':form, 'completed': completed}
    return render(request, 'contact/contact.html', context)
