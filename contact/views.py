from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def addcontact(request):
    form = ContactForm()
    if request.method == 'POST':
	    form = ContactForm(request.POST)
	    if form.is_valid():
		    form.save()
		    return redirect('addcontact')

    total=Contact.objects.all()
    context = {
        'form':form,
        'total':total,
    }
    return render(request, 'Backend/contact/add-contact.html', context)

@login_required(login_url='login')
def updatecontact(request, pk):

	item = Contact.objects.get(id=pk)
	form = ContactForm(instance=item)

	if request.method == 'POST':
		form = ContactForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('addcontact')

	context = {'form':form}
	return render(request, 'Backend/contact/add-contact.html', context)

@login_required(login_url='login')
def deletecontact(request, pk):
	item = Contact.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('addcontact')

	context = {'item':item}
	return render(request, 'Backend/contact/delete-contact.html', context)